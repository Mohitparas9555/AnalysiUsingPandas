#[8:25 PM] Nihal Jaiswal
   # import matplotlib.pyplot as plt
#import pandas as pd
df = pd.read_csv('pokemon.csv')
r=[0,100,200]
plt.hist(x=df['Speed'],bins=r)
plt.show()
