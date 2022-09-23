import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
python=[7,8,6,11,7,8,9]
spark=[2,3,4,3,2,6,5]
pandas=[8,5,7,8,13,5,3]
plt.stackplot(days,python,spark,pandas,labels=['Python','Spark','Pandas'])
plt.legend()
plt.grid()
plt.show()
