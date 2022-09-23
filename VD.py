import matplotlib.pyplot as plt
import seaborn as ss
name = ['nihal','gautam','mamta','sonu','kapil']
score = [9,7,10,5,8]
score2 = [5,9,3,5,7]
plt.bar(name,score,label='Test1')
plt.bar(name,score2,label='Test2',bottom=score2)
plt.legend()
plt.xlabel('student name')
plt.ylabel('student score')
plt.title('test run')
plt.grid()
plt.show()


