import pandas as pd

df = pd.read_csv('exemplo.csv')

df_filtrado = df[df['Categoria'] == 'Periferico']

print(df_filtrado)