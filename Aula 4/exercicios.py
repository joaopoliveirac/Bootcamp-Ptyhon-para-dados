# 1- Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# lista = []

# for i in range(1,10+1):
#     lista.extend([i])

# print(lista)

# 2- Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove('C++')
# linguagens.append('Ruby')
# print(linguagens)

# 3- Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# livros: dict = {
#     'titulo': 'game of thrones',
#     'autor': 'jose da silva',
#     'ano': 2005
# }

# for chave,valor in livros.items():
#     print(chave,valor)

# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# texto = 'meu nome e joao pedro oliveira e estou em busca de uma vaga em engenharia de dados'
# dicionario = {}

# for letra in texto:
#     if letra in dicionario:
#         dicionario[letra] += 1
#     else:
#         dicionario[letra] = 1

# print(dicionario)

# 5- Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista = ["maçã", "banana", "cereja",'cereja','banana']
dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total = 0

for produto in lista:
    if produto in dicionario:
        preco_total += dicionario[produto]
    else:
        pass

print(preco_total)
