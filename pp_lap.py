import math
def ham_lap(x):
    return math.sqrt(1-4*math.sin(x)) 
 
def pp_lap(x, q, ep):
    cnt = 1
    while abs(ham_lap(x) - x) > (ep * (1 - q) / q):
        print(f"x{cnt}              {x:.9f}")
        x = ham_lap(x)
        print(x)
        cnt += 1

def main():
    x = float(input("NHAP GIA TRI X BAT KI TRONG KHOANG CACH LY : "))
    q = float(input("\nNHAP GIA TRI Q-MAX(ABS(F_DERIVATIVE1)) TREN KHOANG CACH LY : "))
    ep = float(input("\nNHAP GIA TRI EPXILON : "))
    pp_lap(x, q, ep)

if __name__ == "__main__":
    main()
    