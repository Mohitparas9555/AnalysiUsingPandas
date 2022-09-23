import pandas as pd
df=pd.read_csv('pokemon.csv')
l=['Grass','Water','Fire','Bug']
df=df.loc[df['Type 1'].isin(l)]
print(df)