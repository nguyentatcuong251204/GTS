import math
import numpy as np
import matplotlib.pyplot as plt
def f_x(a):
    return pow(2,a)-5*a+math.sin(a)

def f_derivative1(a):
    return pow(2,a)*math.log(2)-5+math.cos(a)

def f_derivative2(a):
    return pow(math.log(2),2)*pow(2,a)-math.sin(a)

def dx(x,d):
    return -(f_x(x)*(x-d))/(f_x(x)-f_x(d))
    

def pp_day_cung(a,b,ep):
    x=None
    d=None
    print("x                                                           dx")
    if(f_derivative2((a+b)/2)*f_x(a)>0):
        d=a
        x=b
        tmp=-1
        while(abs(dx(x,d))>0.0005*tmp):
            tmp=x
            x=x+dx(x,d)
            print(x,"                                 ",abs(dx(x,d)))
    else:
        print("a")
        d=b
        x=a
        tmp=-1
        while(abs(dx(x,d))>0.0005*tmp):
            tmp=x
            x=x+dx(x,d)
            print(x,"                                 ",abs(dx(x,d)))


if __name__=="__main__":
    pp_day_cung(4,5,0.000000000001 )