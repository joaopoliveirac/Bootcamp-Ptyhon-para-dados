#1-Calcular Média de Valores em uma Lista
# def calcular_media (lista):
#     media = sum(lista)/len(lista)
#     return media

# numeros = [10,20,69,78]

# print(calcular_media(numeros))

#2-Filtrar Dados Acima de um Limite
# def filtrar_limite (valores, limite):
#     valores_filtrados = []
#     for valor in valores:
#         if valor > limite:
#             valores_filtrados.append(valor)
#     return valores_filtrados

# valores = [5,10,15,20,35,566,-6565]
# limite = 15
# print(filtrar_limite(valores,limite))

#3-Contar Valores Únicos em uma Lista
# def contar_valores_unicos (valores):
#     valores_unicos = []
#     for valor in valores:
#         if valor in valores_unicos:
#             pass
#         else:
#             valores_unicos.append(valor)
#     return len(valores_unicos)

# lista = [1,2,3,3,3,6,9,10,15,12,16,15,16,17,19,20,20,21,23,21,23]
# print(contar_valores_unicos(lista))

#4-Converter Celsius para Fahrenheit em uma Lista
# def conversao (celsius):
#     fahren = []
#     for temperatura in celsius:
#         temp_convertida = 0
#         temp_convertida = (temperatura * 1.8) + 32
#         fahren.append(temp_convertida)
#     return fahren

# celsius = [20,30,40,50,60,100]
# print(conversao(celsius))

#5-Calcular Desvio Padrão de uma Lista
# def calcular_desvio_padrao(valores: List[float]) -> float:
#     media = sum(valores) / len(valores)
#     variancia = sum((x - media) ** 2 for x in valores) / len(valores)
#     return variancia ** 0.5

#6-Encontrar Valores Ausentes em uma Sequência

