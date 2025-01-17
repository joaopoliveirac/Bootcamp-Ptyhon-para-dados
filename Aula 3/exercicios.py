### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# quantidade = 40
# preco = 20

# if quantidade > 0 and preco > 0:
#     print('valores validos')
# else:
#     print('valores invalidos')


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# temperatura = 20

# if temperatura <= 15:
#     print('temperatura baixa')
# elif temperatura > 15 and temperatura <=35:
#     print('temperatura normal')
# else:
#     print('temperatura alta')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'error':
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 45
# email = 'joaopo.0607@gmail.com'

# if not 18 <= idade <=65:
#     print('idade invalida')
# elif not '@' in email or '.' in email:
#     print('email invalido')
# else:
#     print('dados validos')


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor'] > 10000 and 9 < transacao['hora'] > 18:
#     print('transação suspeita!')


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = 'hoje e nossa segunda aula do bootcamp , bootcamp de python'
# texto = texto.replace(',','')
# palavras = texto.split()

# contagem_de_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_de_palavras:
#         contagem_de_palavras[palavra] += 1
#     else:
#         contagem_de_palavras[palavra] = 1

# print(contagem_de_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# lista = [10,20,30,40,50]
# minimo = min(lista)
# maximo = max(lista)

# lista_escala = [(x - minimo) / (maximo - minimo) for x in lista]
# print(lista_escala)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario['email'] ]
# print(usuarios_validos)



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# lista_todos = [2,4,9,7,6,8,95,100,72,93,48,47,63,90]

# lista_pares = [numero for numero in lista_todos if numero % 2 == 0]
# print(lista_pares)


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# venda_categoria = {}

# for venda in vendas:
#     categoria = venda['categoria']
#     valor = venda['valor']
#     if categoria in venda_categoria:
#         venda_categoria[categoria] += valor
#     else:
#         venda_categoria[categoria] = valor

# print(venda_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# lista = []
# dados_entrada = input('informe os dados ou sair para sair.').lower()

# while dados_entrada != 'sair':
#     dados_entrada = input('informe os dados ou sair para sair.').lower()
        
### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = float(input('informe um numero dentro de 1 a 100: '))

# while not 1 < numero < 100:
#     print('numero invalido.')
#     numero = float(input('informe um numero dentro de 1 a 100: '))

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# api = 10

# while api > 0:
#     print('processando os dados!')
#     api -= 1

# print('todas as paginas foram processadas.')

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# tentativa = 0
# limite = 10

# while tentativa < limite:
#     print('tentando conexão')
#     tentativa += 1

# print('tentativas esgotadas.')


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.