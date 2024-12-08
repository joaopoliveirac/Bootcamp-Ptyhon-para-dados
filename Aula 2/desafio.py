#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante 
#e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. 
#Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

nome = input('digite seu nome')
if nome.isdigit():
    print('Voce digitou seu nome errado.')
    exit()
elif len(nome) == 0:
    print('voce nao digitou nada')
    exit()
elif nome.isspace():
    print('voce digitou só espaço')
    exit()

salario = float(input('informe seu salario'))
if salario < 0:
    print('voce digitou um salario negativo.')
    exit()

constante_bonus = 1000

bonus = float(input('informe o bonus recebido em %'))
if bonus < 0:
    print('digitou um bonus negativo.')
    exit()

valor_bonus = constante_bonus + salario * bonus
print(valor_bonus)