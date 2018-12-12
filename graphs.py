

import matplotlib.pyplot as plt
import numpy as np
import random as ra
def linegraph ():
    x = np.linspace(-15, 15, 20)
    y = x**2
    plt.title('Линейный график')
    plt.xlabel('Ось Х')
    plt.ylabel('Ось Y')
    plt.plot(x, y)
    plt.show()
linegraph ()

def bargraph():
    x=[]
    y=[]
    for i in range(10):
        a = ra.randint(1,20)
        b = ra.randint(1,20)
        x.append(a)
        y.append(b) 
    plt.bar(x, y, label='Показатели', color='r')
    plt.title('Столбчатый график')
    plt.xlabel('Ось Х')
    plt.ylabel('Ось Y')
    plt.legend()
    plt.show()
bargraph ()

scatterplot= t = np.linspace(0, 10, 21)
y = t**4
plt.plot(t,y, 'go')    
plt.title('Точечный график')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.legend(['Точки'], loc='best')   
plt.show()
scatterplot ()

