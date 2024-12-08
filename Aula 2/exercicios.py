# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_01 = int(input('Informe o numero 1: '))
# numero_02 = int(input('Informe o numero 2: '))
# soma = numero_01 + numero_02
# print(f'A soma dos números é: {soma}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input('Informe o numero: '))
# resto_divisao = numero % 5
# print(f'O resto da divisão é: {resto_divisao}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_01 = int(input('informe o primeiro numero: '))
# numero_02 = int(input('informe o segundo numero: '))
# multi = numero_01 * numero_02
# print(f'O resultado da multiplicação é: {multi}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_01 = int(input('informe o primerio numero: '))
# numero_02 = int(input('informe o segundo numero'))
# divisao_inteira = numero_01 // numero_02
# print(f'A divisao inteira do primeiro pelo segundo é: {divisao_inteira}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input('Informe o numero'))
# quadrado = numero ** 2
# print(f'O quadrado do numero informado é: {quadrado}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_01 = float(input('informe o primeiro numero: '))
# numero_02 = float(input('informe o segundo numero: '))
# soma = numero_01 + numero_02
# print(f'A soma é: {soma}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_01 = float(input('informe o primeiro numero: '))
# numero_02 = float(input('informe o segundo numero: '))
# media = (numero_01 + numero_02) / 2
# print(f'A média é: {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero_base = float(input('Informe a base da potencia: '))
# numero_expoente = float(input('Informe o expoente da potencia: '))
# potencia = numero_base ** numero_expoente
# print(f'A potencia é: {potencia}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temp_celsius = float(input('informe a temperatura em celsius: '))
# conversao = (temp_celsius * 9/5) + 32
# print(f'A temperatura em Fahrenheit é: {conversao}')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input('Digite o raio: '))
# area = 3.14 * raio ** 2
# print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = input('informe uma palavra ou frase').upper()
# print(texto)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input('informe o nome do usuario').lower()
# print(nome)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input('informe uma frase.')
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input('informe a data no formato dd/mm/aaaa').split('/')
# print(data)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto_01 = input('informe a primeira frase')
# texto_02 = input('informe a segunda frase')
# print(texto_01 + texto_02)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# bool_01 = input('informe o primeiro valor booleano')
# bool_02 = input('informe o segundo valor booleano')
# bool_01 = bool_01.lower() == 'true'
# bool_02 = bool_02.lower() == 'true'
# resultado = bool_01 and bool_02
# print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# bool_01 = input('informe o primeiro valor booleano')
# bool_02 = input('informe o segundo valor booleano')
# bool_01 = bool_01.lower() == 'true'
# bool_02 = bool_02.lower() == 'true'
# resultado = bool_01 or bool_02
# print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C é igual a {fahrenheit}°F.")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")
# 22: Verificador de Palíndromo
# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
# try:
#     numero1 = float(input('digite o primeiro numero'))
#     numero2 = float(input('digite o segundo numero'))
#     operador = input("Digite o operador (+, -, *, /): ")
#     if operador == '+':
#         resultado = numero1 + numero2
#     elif operador == '-':
#         resultado = numero1 - numero2
#     elif operador == '*':
#         resultado = numero1 * numero2
#     elif operador == '/':
#         resultado = numero1 / numero2
#     else:
#         print('operador invalido ou divisao por zero.')
#     print(resultado)
# except ValueError:
#     print('entrada invalida, insira números.')

# 24: Classificador de Números
# 25: Conversão de Tipo com Validação