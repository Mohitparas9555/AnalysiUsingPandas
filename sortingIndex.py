import pandas as pd

df=pd.read_csv('heroes.csv')
df=df.set_index(['Alignment','Publisher'])
df=df.sort_index(level=['Alignment','Publisher'])
#df=df.loc[('bad','Dark Horse Comic'):('good','Marvel Comics')]
df=df.loc[('bad','Dark Horse Comic'):('good','Marvel Comics'),'name':'Race'] #(with colums accces)
df.to_csv('r.csv')
print(df)