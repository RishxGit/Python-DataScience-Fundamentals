import matplotlib.pyplot as plt
import numpy as np

#basic
'''
x = np.array([2023,2024,2025,2026])
y = np.array([15,25,30,20])

plt.plot(x,y)

plt.show()
'''

#bar chart
'''
categories = np.array(['grains','fruit','vegs','protien','dairy','sweets'])
values = np.array([4,3,2,5,3,1])

plt.bar(categories,values)

plt.title('Daily consumption')
plt.xlabel('FOOD')
plt.ylabel('Quantity')

plt.show()
'''

#Scatter graph

'''
x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) #hours studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) #grades


x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

plt.scatter(x1,y1, label='Class A')
plt.scatter(x2,y2, label='Class b')

plt.title('Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Grades')

plt.legend()
plt.show()

'''
#Histogram
'''
scores = np.random.normal(loc=80,scale=10,size= 100)
scores = np.clip(scores,0,100)

plt.hist(scores, bins= 10, color='lightblue',edgecolor= 'black')

plt.title('Exam scores')
plt.xlabel('SCORES')
plt.ylabel('# of students')

plt.show()
'''

#graph with pandas
'''
import pandas as pd 


df = pd.read_csv('data.csv')

type_count = df['Type1'].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values,edgecolor= 'black')

plt.title('# of pokemon by type')
plt.xlabel('count')
plt.ylabel('type')
plt.tight_layout
plt.show()
'''

#sub plots
'''
x = np.array([1,2,3,4,5])

figure, axes = plt.subplots(2,2)


axes[0,0].plot(x, x*2)
axes[0,0].set_title('x*2')

axes[0,1].plot(x, x**2)
axes[0,1].set_title('x**2')

axes[1,0].plot(x, x**3)
axes[1,0].set_title('x**3')

axes[1,1].plot(x, x**4)
axes[1,1].set_title('x**4')


plt.tight_layout
plt.show()
'''