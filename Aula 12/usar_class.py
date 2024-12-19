from class_csv import CsvProcessor


arquivo_csv = './exemplo.csv'
filtro = 'Categoria'
valor = 'Periferico'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro,valor))


arquivo_csv_2 = './exemplo_2.csv'
arquivo_CSV2 = CsvProcessor(arquivo_csv_2)
arquivo_CSV2.carregar_csv()
print(arquivo_CSV2.filtrar_por(filtro,'teste'))