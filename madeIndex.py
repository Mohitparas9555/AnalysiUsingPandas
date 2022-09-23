import pandas as pd
df=pd.read_csv('heroes.csv')
df=df.set_index('Publisher')
l=['Marvel Comics','DC Comics']
df=df.sort_index()
df=df.loc['ABC Studios':'Marvel Comics']
df.to_csv('m.csv')

print(df)