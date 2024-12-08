class Livro:
    def __init__(self, titulo, autor, isbn, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade = quantidade

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Quantidade: {self.quantidade}")

    def verificar_disponibilidade(self):
        return self.quantidade > 0


class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}, Livros Emprestados: {[livro.titulo for livro in self.livros_emprestados]}")

    def emprestar_livro(self, livro):
        if livro.verificar_disponibilidade():
            if len(self.livros_emprestados) < self.limite_emprestimos():
                self.livros_emprestados.append(livro)
                livro.quantidade -= 1
                print(f"Livro '{livro.titulo}' emprestado com sucesso.")
            else:
                print("Limite de livros emprestados atingido.")
        else:
            print(f"O livro '{livro.titulo}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.quantidade += 1
            print(f"Livro '{livro.titulo}' devolvido com sucesso.")
        else:
            print(f"O livro '{livro.titulo}' não foi emprestado por você.")

class Aluno(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.turmas_matriculadas = []

    def matricular_turma(self, turma):
        if turma not in self.turmas_matriculadas:
            self.turmas_matriculadas.append(turma)
            turma.adicionar_aluno(self)
            print(f"Aluno {self.nome} matriculado na turma {turma.codigo}.")
        else:
            print(f"Aluno {self.nome} já está matriculado na turma {turma.codigo}.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}, Turmas Matriculadas: {[turma.codigo for turma in self.turmas_matriculadas]}")

class Professor(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)
        print(f"Turma {turma.codigo} adicionada à disciplina {self.nome}.")

    def exibir_turmas(self):
        print(f"Turmas da disciplina {self.nome}:")
        for turma in self.turmas:
            turma.exibir_alunos()

class Turma:
    def __init__(self, codigo, disciplina):
        self.codigo = codigo
        self.disciplina = disciplina
        self.alunos = []
        self.avaliacoes = {}

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.matricular_turma(self)
        else:
            print(f"Aluno {aluno.nome} já está na turma {self.codigo}.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.turmas_matriculadas.remove(self)
            print(f"Aluno {aluno.nome} removido da turma {self.codigo}.")
        else:
            print(f"Aluno {aluno.nome} não está na turma {self.codigo}.")

    def registrar_avaliacao(self, aluno, avaliacao):
        self.avaliacoes[aluno] = avaliacao
        print(f"Avaliação registrada para o aluno {aluno.nome} na turma {self.codigo}.")

    def exibir_alunos(self):
        print(f"Alunos na turma {self.codigo}:")
        for aluno in self.alunos:
            print(aluno.nome)

    def exibir_avaliacoes(self):
        print(f"Avaliações da turma {self.codigo}:")
        for aluno, avaliacao in self.avaliacoes.items():
            print(f"Aluno: {aluno.nome}, Nota: {avaliacao.nota}, Peso: {avaliacao.peso}")

class Avaliacao:
    def __init__(self, nota, peso):
        self.nota = nota
        self.peso = peso

    def calcular_nota_final(self):
        return self.nota * self.peso

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.disciplinas = []
        self.turmas = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")  

    def cadastrar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        print(f"Disciplina '{disciplina.nome}' cadastrada com sucesso.")

    def cadastrar_turma(self, turma):
        self.turmas.append(turma)
        print(f"Turma '{turma.codigo}' cadastrada com sucesso.")

    def listar_livros(self):
        print("\nLivros cadastrados:")
        for livro in self.livros:
            livro.exibir_detalhes()

    def listar_usuarios(self):
        print("\nUsuários cadastrados:")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")  
        for usuario in self.usuarios:
            usuario.exibir_informacoes()

    def listar_disciplinas(self):
        print("\nDisciplinas cadastradas:")
        for disciplina in self.disciplinas:
            print(disciplina.nome)

    def listar_turmas(self):
        print("\nTurmas cadastradas:")
        for turma in self.turmas:
            print(f"Turma {turma.codigo} da disciplina {turma.disciplina.nome}")


def menu():
    biblioteca = Biblioteca()  
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo livro")
        print("2. Cadastrar novo usuário")
        print("3. Cadastrar nova disciplina")
        print("4. Cadastrar nova turma")
        print("5. Matricular aluno em turma")
        print("6. Registrar avaliação de aluno")
        print("7. Listar livros")
        print("8. Listar usuários")
        print("9. Listar disciplinas")
        print("10. Listar turmas")
        print("11. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            isbn = input("ISBN do livro: ")
            quantidade = int(input("Quantidade do livro: "))
            livro = Livro(titulo, autor, isbn, quantidade)
            biblioteca.cadastrar_livro(livro)

        elif opcao == '2':
            
            print("Entrando no cadastro de usuário...")  
            tipo_usuario = input("Tipo de usuário (Aluno/Professor): ").strip().lower()
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")

            if tipo_usuario == 'aluno':
                usuario = Aluno(nome, email)
            elif tipo_usuario == 'professor':
                usuario = Professor(nome, email)
            else:
                print("Tipo de usuário inválido.")
                continue

            biblioteca.cadastrar_usuario(usuario)  
            print(f"Usuário {usuario.nome} cadastrado com sucesso!")  

        elif opcao == '3':
            nome_disciplina = input("Nome da disciplina: ")
            disciplina = Disciplina(nome_disciplina)
            biblioteca.cadastrar_disciplina(disciplina)

        elif opcao == '4':
            codigo_turma = input("Código da turma: ")
            disciplina_nome = input("Nome da disciplina: ")
            disciplina = next((d for d in biblioteca.disciplinas if d.nome == disciplina_nome), None)
            if disciplina:
                turma = Turma(codigo_turma, disciplina)
                biblioteca.cadastrar_turma(turma)
            else:
                print("Disciplina não encontrada.")

        elif opcao == '5':
            nome_aluno = input("Nome do aluno: ")
            codigo_turma = input("Código da turma: ")
            aluno = next((u for u in biblioteca.usuarios if u.nome == nome_aluno and isinstance(u, Aluno)), None)
            turma = next((t for t in biblioteca.turmas if t.codigo == codigo_turma), None)
            if aluno and turma:
                aluno.matricular_turma(turma)
            else:
                print("Aluno ou turma não encontrados.")

        elif opcao == '6':
            nome_aluno = input("Nome do aluno: ")
            codigo_turma = input("Código da turma: ")
            aluno = next((u for u in biblioteca.usuarios if u.nome == nome_aluno and isinstance(u, Aluno)), None)
            turma = next((t for t in biblioteca.turmas if t.codigo == codigo_turma), None)
            if aluno and turma:
                nota = float(input("Nota: "))
                peso = float(input("Peso: "))
                avaliacao = Avaliacao(nota, peso)
                turma.registrar_avaliacao(aluno, avaliacao)
            else:
                print("Aluno ou turma não encontrados.")

        elif opcao == '7':
            biblioteca.listar_livros()

        elif opcao == '8':
            biblioteca.listar_usuarios()

        elif opcao == '9':
            biblioteca.listar_disciplinas()

        elif opcao == '10':
            biblioteca.listar_turmas()

        elif opcao == '11':
            print("Obrigado...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    biblioteca = Biblioteca()  
    menu()
