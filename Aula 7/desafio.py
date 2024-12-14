#Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, 
#processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.
import csv

path_arquivo = 'vendas.csv'

def ler_csv(nome_arquivo_csv):
    """
    funcao que le um arquivo csv e retorna uma lista de dicionario
    
    """
    dicionario = {}
    with open (nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            #print(linha)
            categoria = linha['Categoria']
            produto = linha['Produto']
            quantidade = linha['Quantidade']
            venda = linha['Venda']

            dados_produto = {'Produto': produto,
                             'Quantidade': quantidade,
                             'Venda': venda}
            
            if categoria not in dicionario:
                dicionario[categoria] = []
            
            dicionario[categoria].append(dados_produto)
    return dicionario


def calcular_vendas_categoria(dicionario_processado):
    total_categoria = {}

    for categoria, produtos in dicionario_processado.items():
        total_vendas = 0
        #print(categoria)

        for produto in produtos:
            produto['Quantidade'] = float(produto['Quantidade'])
            produto['Venda'] = float(produto['Venda'])

            total_vendas += produto['Quantidade'] * produto['Venda']
        
        total_categoria[categoria] = total_vendas
    return total_categoria


vendas_itens = ler_csv(path_arquivo)
print(calcular_vendas_categoria(vendas_itens))


