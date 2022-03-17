import matplotlib.pyplot as plt
import numpy as np 

x = []
y = []

for _ in range(100):
    x.append(np.random.randint(0,100))
    y.append(np.random.randint(0,100))


plt.scatter(x=x,y=y)
plt.plot(np.linspace(0,100,100),np.linspace(0,100,100), color='r')
plt.xlabel('test')
plt.ylabel('test1')

plt.show()
