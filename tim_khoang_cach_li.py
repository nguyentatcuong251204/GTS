import numpy as np
import matplotlib.pyplot as plt
# HÀM ĐA THỨC
def ham(a,x):
    n=len(a)
    result=0
    for i in range(n):
        result+=a[i]*pow(x,(n-1-i))
    return result
def dao_ham(a,x):
    n=len(a)
    result=0
    for i in range(n):
        result+=(n-i-1)*a[i]*pow(x,(n-2-i))
    return result
def ban_kinh_nghiem(a):
    return 1+max(abs(np.array(a))/abs(a[0]))

def main():
    a=[1,2,-3]
    r=ban_kinh_nghiem(a)
    print("BÁN KÍNH NGHIỆM ")
    print(r)
    x1=-r
    x2=-r
    while(x1<r):
        anpha=0.001
        n=0
        dao_ham_bac1=dao_ham(a,x1)
        if(dao_ham_bac1<0):
            while n<10000:
                x1=x1-anpha*dao_ham_bac1
                n+=1
                if ham(a,x1)*ham(a,x2)<0:
                    print(x2," ",x1," LÀ KHOẢNG CÁCH LY NGHIỆM ")
                    x2=x1
                    break
                else:
                    # print(x2," " ,x1 ," KHÔNG LÀ KHOẢNG CÁCH LY NGHIỆM")
                    x2=x1
        else:
            while n<100000:
                x1=x1+anpha*dao_ham_bac1
                n+=1
                if ham(a,x2)*ham(a,x1)<0:
                    print(x2," ",x1," LÀ KHOẢNG CÁCH LY NGHIỆM ")
                    x2=x1
                    break
                else:
                    # print(x2," " ,x1 ," KHÔNG LÀ KHOẢNG CÁCH LY NGHIỆM")
                    x2=x1
        
if __name__=="__main__":
    main()