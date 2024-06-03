import numpy as np

def f(x):
    # Định nghĩa hàm f(x) cho hệ phương trình phi tuyến
    return np.array([
        4*x[0] ** 2 -20*x[0] + 1/4*pow(x[1],2)+8,  # Phương trình của hình tròn
        1/2*x[0]*pow(x[1],2) + 2*x[0] -5*x[1]+8              # Phương trình phi tuyến khác
    ])

def jacobian_f(x):
    # Tính ma trận Jacobi của hàm f(x)
    return np.array([
        [8*x[0]-20, 1/2 * x[1]],         # Phần đạo hàm riêng theo x[0]
        [1/2*pow(x[1],2)+2, x[0]-5]           # Phần đạo hàm riêng theo x[1]
    ])

def newton_method(f, jacobian_f, x0, tol=1e-6, max_iter=100):
    # Hàm thực hiện thuật toán Newton
    x = x0
    for i in range(max_iter):
        print(x,end="      ")
        print(np.linalg.det(jacobian_f(x)))

        dx = np.linalg.solve(jacobian_f(x), -f(x)) # Giải hệ phương trình tuyến tính
        x = x + dx
        if np.linalg.norm(dx,ord=np.inf) < tol:
            break


# Điểm bắt đầu
x0 = np.array([0, 0])

# Giải hệ phương trình phi tuyến bằng phương pháp Newton
newton_method(f, jacobian_f, x0)

