import numpy as np
import matplotlib.pyplot as plt
# HÀM ĐA THỨC
def ham(a,x):
    n=len(a)
    result=0
    for i in range(n):
        result+=a[i]*x**(n-1-i)
    return result
def ban_kinh_nghiem(a):
    return 1+max(abs(np.array(a))/abs(a[0]))
def main():
    a=[1,-6,11,-6]
    r=ban_kinh_nghiem(a)
    print(r)
    x=np.linspace(0,4,1000000)
    x=list(x)
    y=[ham(a,k) for k in x ]
    truc_hoanh=[0 for k in x]
    plt.plot(x,y)
    plt.plot(x,truc_hoanh)
    plt.show()
if __name__ == '__main__':
    main()
