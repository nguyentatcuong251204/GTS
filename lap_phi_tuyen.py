import numpy as np

def f(x):
    # Định nghĩa hàm f(x) cho hệ phương trình phi tuyến
    return np.array([
        x[0] ** 2 + x[1] ** 2 - 1,  # Phương trình của hình tròn
        x[0] - x[1] ** 3              # Phương trình phi tuyến khác
    ])

def jacobian_f(x):
    # Tính ma trận Jacobi của hàm f(x)
    return np.array([
        [2 * x[0], 2 * x[1]],         # Phần đạo hàm riêng theo x[0]
        [1, -3 * x[1] ** 2]           # Phần đạo hàm riêng theo x[1]
    ])

def theta(x):
    return np.array(
        [
            x[1]**3,
            np.sqrt(1-x[0]**2)
        ]
    )

def j(x):
    return np.array(
        [[0,3*x[1]**2],[-x[0]/np.sqrt(1-x[0]**2),0]]
    )


def calculate_k(x):
    return np.linalg.norm(j(x),ord=np.inf)

def main():
    ep=0.000001
    x=np.array([0.5,0.5])
    print("KHỞI TẠO GIÁ TRỊ X0,X1 BAN ĐẦU ")
    print(x)
    print("HỆ SỐ CO ")
    k=calculate_k(x)
    print(k)
    cnt=1
    while(np.linalg.norm(theta(x)-x,ord=np.inf)>ep*(1-k)/k):
        x=theta(x)
        print(x)
        print(k)
        
        # break
        
                    


if __name__=="__main__":
    main()