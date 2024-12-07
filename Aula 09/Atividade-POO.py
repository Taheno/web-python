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


class Usuario:
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


    def limite_emprestimos(self):
        raise NotImplementedError("Esta função deve ser implementada nas subclasses.")


class Aluno(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def limite_emprestimos(self):
        return 3  


class Professor(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def limite_emprestimos(self):
        return 5


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")

    def listar_livros(self):
        print("\nLivros cadastrados:")
        for livro in self.livros:
            livro.exibir_detalhes()

    def listar_usuarios(self):
        print("\nUsuários cadastrados:")
        for usuario in self.usuarios:
            usuario.exibir_informacoes()

    def realizar_emprestimo(self, usuario, livro):
        usuario.emprestar_livro(livro)

    def realizar_devolucao(self, usuario, livro):
        usuario.devolver_livro(livro)


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu:")
        print("1. Cadastrar novo livro")
        print("2. Cadastrar novo usuário")
        print("3. Realizar empréstimo")
        print("4. Realizar devolução")
        print("5. Listar livros")
        print("6. Listar usuários")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            isbn = input("ISBN do livro: ")
            quantidade = int(input("Quantidade do livro: "))
            livro = Livro(titulo, autor, isbn, quantidade)
            biblioteca.cadastrar_livro(livro)

        elif opcao == '2':
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

        elif opcao == '3':
            usuario_nome = input("Nome do usuário: ")
            livro_titulo = input("Título do livro: ")

            usuario = next((u for u in biblioteca.usuarios if u.nome == usuario_nome), None)
            livro = next((l for l in biblioteca.livros if l.titulo == livro_titulo), None)

            if usuario and livro:
                biblioteca.realizar_emprestimo(usuario, livro)
            else:
                print("Usuário ou livro não encontrado.")

        elif opcao == '4':
            usuario_nome = input("Nome do usuário: ")
            livro_titulo = input("Título do livro: ")

            usuario = next((u for u in biblioteca.usuarios if u.nome == usuario_nome), None)
            livro = next((l for l in biblioteca.livros if l.titulo == livro_titulo), None)

            if usuario and livro:
                biblioteca.realizar_devolucao(usuario, livro)
            else:
                print("Usuário ou livro não encontrado.")

        elif opcao == '5':
            biblioteca.listar_livros()

        elif opcao == '6':
            biblioteca.listar_usuarios()

        elif opcao == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
