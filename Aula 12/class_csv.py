import pandas as pd


class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]
        

# arquivo_csv = './exemplo.csv'
# filtro = 'Categoria'
# valor = 'Periferico'

# arquivo_CSV = CsvProcessor(arquivo_csv)
# arquivo_CSV.carregar_csv()
# print(arquivo_CSV.filtrar_por(filtro,valor))


# arquivo_csv_2 = './exemplo_2.csv'
# arquivo_CSV2 = CsvProcessor(arquivo_csv_2)
# arquivo_CSV2.carregar_csv()
# print(arquivo_CSV2.filtrar_por(filtro,'teste'))
        