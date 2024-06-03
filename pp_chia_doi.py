import math

def sign(a):
    if(a>0):return "+"
    else:return "-"

def f_x(a):
    return math.log(a)-1

def pp_chia_doi(a,b,epxilon):
    cnt=0
    m=a
    n=b
    print("STT           a           b           xn            sign           denta_xn")
    while((n-m) > epxilon):
        c=(m+n)/2
        if(f_x(c) == 0):
            print("Nghiệm là ",c)
        else:
            print(cnt,"           ",m,"           ",n,"           ",c,"           ",sign(f_x(c)),"           ",(n-m)/2)
            if(f_x(c)*f_x(m)>0):
                m=c
            elif(f_x(c)*f_x(n)>0):
                n=c
        cnt+=1
# if __name__=="__main__":
a=float(input("NHAP a : "))
b=float(input("NHAP b : "))
epx=float(input("NHAP epxilon : "))
pp_chia_doi(a,b,epxilon=epx)

        

