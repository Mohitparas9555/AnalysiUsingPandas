import matplotlib.pyplot as plt
import numpy as np

name = ['nihal','gautam','mamta','sonu','kapil']
num1 = [9,7,10,5,8]
num2 = [5,9,3,5,7]
X_axis = np.arange(len(name))
plt.bar(X_axis-0.2,num1,0.4,color='red',label='num1')
plt.bar(X_axis+0.2,num2,0.4,color='orange',label='num2')
plt.xticks(X_axis,name)
plt.xlabel('student name')
plt.ylabel('student score')
plt.title('test run')
plt.grid()
plt.show()