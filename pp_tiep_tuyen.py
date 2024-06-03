import math

def f_x(a):
    return math.log(a) - 1

def f_derivative1(a):
    return 1 / a

def f_derivative2(a):
    return -1 / a ** 2

def dx(x):
    return -f_x(x) / f_derivative1(x)

def pp_tiep_tuyen(a, b, ep):
    print("x                                           dx")
    if f_derivative2((a + b) / 2) * f_x(a) > 0:
        x = a
        while abs(dx(x)) > ep:
            print('{:.15f}'.format(x), end="                                            ")
            print('{:.15f}'.format(abs(dx(x))))
            x = x + dx(x)
    else:
        x = b
        while abs(dx(x)) > ep:
            print('{:.15f}'.format(x), end="                                            ")
            print('{:.15f}'.format(abs(dx(x))))
            x = x + dx(x)

pp_tiep_tuyen(1, 3, 0.00000000001)
