import numpy as np
import pandas as pd
def echelon_form(matrix):
    m, n = matrix.shape
    A = matrix.copy().astype(float)
    row = 0
    for col in range(n):
        if row >= m:
            break
        
        # Tìm hàng có phần tử khác 0 ở cột 'col'
        pivot_row = row
        while pivot_row < m and A[pivot_row, col] == 0:
            pivot_row += 1
        
        if pivot_row == m:
            continue  # Nếu không tìm thấy pivot, di chuyển đến cột tiếp theo
        
        # Đưa hàng chứa pivot về đầu tiên (swap)
        print("Phần tử khử là a{}{}".format(pivot_row+1,col+1))
        A[[row, pivot_row]] = A[[pivot_row, row]]
        if pivot_row!=row:
            print("Đưa hàng thứ ",pivot_row+1," về hàng thứ ",row+1)
            print(A)
        # Chuẩn hóa pivot thành 1

        A[row] /= A[row, col]
        print("MA TRẬN SAU KHI ĐƯỢC CHUẨN HÓA ")
        print(A)
        # Khử các phần tử dưới pivot
        for i in range(row + 1, m):
            if A[i, col] != 0:
                A[i] -= A[i, col] * A[row]

        print("MA TRẬN SAU KHI ĐĂ KHỬ CÁC PHẦN TỬ DƯỚI HÀNG THỨ",row+1,"NẰM Ở CỘT THỨ",col+1)
        print(A)
        row += 1
        print("-----------------------------------------------------------------")
    return A

# Ví dụ sử dụng
matrix = np.array([[5, 2, 0, 3],
                   [0, 0, 3, 4],
                   [1, 1, 0, 2]])
print("MA TRẬN GỐC ")
file=open("D:\giai_tich_so\input_gauss_py.txt")
matrix=[line.split() for line in file]
matrix=np.array(matrix)
print(matrix)
A=np.zeros((matrix.shape[0],matrix.shape[1]))

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        A[i][j]=float(matrix[i][j])
print(A)
echelon_matrix = echelon_form(A)                   
print("Ma trận bậc thang:")
print(echelon_matrix)

print("result ")
print(np.linalg.inv(echelon_matrix[:,:-1])@echelon_matrix[:,-1])