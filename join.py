import pandas as pd
for df in pd.read_csv('pokemon.csv',chunksize=100):
    print(df)
