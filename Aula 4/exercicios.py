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
# lista = ["maçã", "banana", "cereja",'cereja','banana']
# dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# preco_total = 0

# for produto in lista:
#     if produto in dicionario:
#         preco_total += dicionario[produto]
#     else:
#         pass

# print(preco_total)

# 6- Objetivo: Dada uma lista de emails, remover todos os duplicados.
# emails = ['joaopo@gmail.com', 'fernanda@gmail.com', 'joaopedro@gmail.com', 'joaopo@gmail.com']
# emails_unico = []

# for email in emails:
#     if email not in emails_unico:
#         emails_unico.append(email)
#     else:
#         pass

# print(emails_unico)

# 7- Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [1,7,9,18,19,20,23,27,9,2,3,7,9,15,166,189,120]

# idade_acima_18 = [idade for idade in idades if idade >= 18]
# print(idade_acima_18)

# 8- Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Breno", "idade": 25, "cidade": "São Paulo", "profissão": "Engenheira"},
#     {"nome": "Josefino", "idade": 30, "cidade": "Rio de Janeiro", "profissão": "Designer"},
#     {"nome": "Alice", "idade": 22, "cidade": "Belo Horizonte", "profissão": "Estudante"},
#     {"nome": "Carla", "idade": 35, "cidade": "Curitiba", "profissão": "Professor"},
#     {"nome": "Manuel", "idade": 28, "cidade": "Porto Alegre", "profissão": "Advogada"}
# ]

# pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa['nome'])

# print(pessoas_ordenadas)

# 9- Objetivo: Dado um conjunto de números, calcular a média.
# numeros = [30,77,99,66,33,35,13,123.60,129,60,199]

# media = sum(numeros)/len(numeros)
# print(f'{media:.2f}')

# 10- Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# valores = [10,30,77,99,60,87,69,30,963,1235,35697,31058,131,1323,314979,13198198,198189,123165,321159,13215132]
# valores_par = []
# valores_impar = []

# for valor in valores:
#     if valor % 2 == 0:
#         valores_par.append(valor)
#     else:
#         valores_impar.append(valor)

# print(f'Valores par: {valores_par}. Valores impar: {valores_impar}')

# 11- Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [
#     {"id": 1, "nome": "Notebook", "preco": 3500.00, "estoque": 10},
#     {"id": 2, "nome": "Mouse", "preco": 50.00, "estoque": 150},
#     {"id": 3, "nome": "Teclado", "preco": 120.00, "estoque": 80},
#     {"id": 4, "nome": "Monitor", "preco": 950.00, "estoque": 25},
#     {"id": 5, "nome": "Impressora", "preco": 600.00, "estoque": 5}
# ]
# atualizar = produtos[1]['preco'] = 5000000
# print(produtos[1]['preco'])

# 12- Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}
# print(dicionario_fundido)


# 13- Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# estoque = {
#     "Notebook": {"quantidade": 10, "preco": 3500.00},
#     "Mouse": {"quantidade": 150, "preco": 50.00},
#     "Teclado": {"quantidade": 0, "preco": 120.00},
#     "Monitor": {"quantidade": 25, "preco": 950.00},
#     "Impressora": {"quantidade": 0, "preco": 600.00}
# }
# produtos_estoque = []

# for produto in estoque:
#     if estoque[produto]['quantidade'] > 0:
#         produtos_estoque.append({produto})
#     else:
#         pass

# print(produtos_estoque)
    
# 14- Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
# dicionario = {'joao': 3, 'pedro': 60, 'jose':99, 'serafo': 155}
# chaves = []
# valores = []

# for chave, valor in dicionario.items():
#     chaves.append(chave)
#     valores.append(valor)

# print(chaves)
# print(valores)

# 15- Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
# frase = 'meu nome e joao pedro oliveira e eu to procurando um emprego como engenheiro de dados'
# dicionario_frequencia = {}

# for letra in frase:
#     if letra not in dicionario_frequencia:
#         dicionario_frequencia[letra] = 1
#     else:
#         dicionario_frequencia[letra] +=1

# print(dicionario_frequencia)

# 16- Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# def recebe_lista (lista):
#     return sum(lista)

# numeros = [10,20,30,40,55]
# print(recebe_lista(numeros))

# 17- Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

# 18- Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# def reverter_texto (texto):
#     return texto[::-1]

# print(reverter_texto('joaopedro'))

# 19- Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# def combinacao (lista,numero):
#     soma = []
#     for valor in lista:
#         soma.append(valor+numero)
#     return soma

# lista_numeros = [10,30,55,100,200,6600]

# print(combinacao(lista_numeros,10))

# 20- Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# def ordenar (dicionario):
#     lista = []
#     for chave, valor in dicionario.items():
#         lista.append(chave)
#     lista.sort()
    
#     return lista

# dicionario = {'joao': 1,'pedro':2,'alice':6,'bruna':7}
# print(ordenar(dicionario))