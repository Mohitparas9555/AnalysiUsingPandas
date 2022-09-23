import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
df = sns.load_dataset("tips")
sns.relplot(x='total_bill',y='tip',data=df,hue='smoker',size='size',kind='line',col='day')
plt.show()





