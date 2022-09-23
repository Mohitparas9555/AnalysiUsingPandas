import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('pokemon.csv')
g=df['Generation'].value_counts().reset_index()
print(g)
plt.pie(g['Generation'],labels=g['index'],autopct='%1.2f%%')
plt.show()