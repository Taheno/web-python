# Listas e Dicionários

# LISTAS

numeros =[ 1,2,3,4,5,6]

# Inserir elementos
numeros.append(7)
numeros.insert(2,"dois")

# Remover Elementos
numeros.pop(1) # Remove pelo indice
numeros.remove("dois") # Remove pelo valor

# numeros.sort()
# numeros.reverse()

# print(numeros[0]) # Primeiro elemento
# print(numeros[-1]) # Ultimo elemento
# print(numeros)

# resp = input(f'Deseja remover algum elemento da lista {numeros}? (s/n)').lower
# if resp == 's':

pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
