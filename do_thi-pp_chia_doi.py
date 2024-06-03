import matplotlib.pyplot as plt
import math
def plot(x,y):
    plt.plot(x,y)
    plt.show()     


def f(x):
    return pow(x,2)+4*math.sin(x)-1
x,y,z=[],[],[]
for i in range(-100,100,1):
    x.append(i/10)
    y.append(f(i/10))
    z.append(0)

# plt.plot(x,y,label='lnx-1',color='red')
# plt.plot(x,z,label='y=0',color='blue')
# plt.legend()
# plt.show()
plt.plot(x,y)
plt.plot(x,z)
plt.show()

print(f(-2.4))