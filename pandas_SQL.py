import pandas as pd
from pandasql import sqldf

df = pd.read_csv('pokemon.csv')
df2 = sqldf("SELECT * FROM df WHERE Name='Bulbasaur'", globals())


print(df2)

# import os
# os.mkdir(r'C:\Users\nihal\OneDrive\Desktop\Data2\nihal')
# mysql=lambda q:sqldf(q,globals())
