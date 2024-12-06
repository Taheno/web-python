class Livro:
    def __init__(self, titulo, autor, isbn, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade = quantidade
    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor},
        ISBN: {self.isbn}, Quantidade: {self.quantidade}")
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
            self.livros_emprestados.append(livro)
            livro.quantidade -= 1
        else:
            print(f"O livro '{livro.titulo}' não está disponível.") 

   