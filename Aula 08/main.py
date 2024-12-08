class Livro:
    def __init__(self, titulo, autor, edicao, qtd_pagina):
        self.titulo = titulo
        self.autor = autor
        self.edicao =edicao
        self.qtd_pagina = qtd_pagina
    
    def exibir_detalhes(self):
        return(f'Titulo: {self.titulo}, Autor: {self.autor}, Edição: {self.edicao}')
    
    def atualizar_livro():
        pass

    def __str__(self):
        return(f'Titulo: {self.titulo}, Autor: {self.autor}, Edição: {self.edicao}')

livro1 = Livro('Fundamentos de Python', 'Fulano de Tal', '2022', '215')
livro2 = Livro('Logica de Programação', 'Ciclano de Tal', '2019', '323')

print(livro1.exibir_detalhes())
print(livro2.exibir_detalhes())
print(livro1)

livro3 = Livro('Livro três', 'Ciclano de Tal', '2015', '88')
livro4 = Livro('POO para iniciantes', 'Um Autor Qualquer', '2012', '123')
livro5 = Livro('Banco de dados com Python', 'José da Silva', '2021', '201')
livro6 = Livro('Livro Seis', 'Um Dois três da Silva Quatro', '2023', '501')


class Produto:
    def __init__(self, nome, marca, preco, quantidade, ativo):
        self.nome = nome
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade
        self.ativo = ativo

    def atualiza_preco(self):
        self.preco = input("Informe o valor ")

    def mostra_preco(self):
        return(f'Preço: R$ {self.preco}')
    
    def __str__(self):
        return(f'Produto: {self.nome}, marca: {self.marca}, Preço Unitário: R$ {self.preco}')

produto1 = Produto("Caneta", "BIC", 0.50, 100, 1 )

print(produto1)

print(produto1.mostra_preco())
produto1.atualiza_preco()
print(produto1)
        






