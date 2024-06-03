import numpy as np
import pandas as pd
def LU_decomposition(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j][j] = 1

        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = matrix[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            if U[j][j]==0:
                print("MA TRẬN U")
                print(U)
                print("GIÁ TRỊ TRÊN ĐƯỜNG CHÉO CHÍNH CỦA MA TRẬN U BẰNG 0, K THỂ THỰC HIỆN THUẬT TOÁN ")
                return None,None
            else:
                L[i][j] = (matrix[i][j] - s2) / U[j][j]

    return L, U

# Example usage
# matrix = np.array([[4, 3, -2], [2, 1, -3], [1, 3, -1]])
file=open("D:\giai_tich_so\input_LU_giai_hpt.txt")
matrix=[line.split() for line in file]
matrix=np.array(matrix)
A=np.zeros((matrix.shape[0],matrix.shape[1]-1))
b=np.zeros((matrix.shape[0],1))


for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]-1):
        A[i][j]=float(matrix[i][j])
print("Ma trận A")
print(A)
for i in range(matrix.shape[0]):
    b[i][0]=float(matrix[i][-1])

print("Ma trận b")
print(b)
if(np.linalg.det(A)==0):
    print("ĐỊNH THỨC CỦA MA TRẬN BẰNG 0, KHÔNG THỂ THỰC HIỆN THUẬT TOÁN")
else:
    L, U = LU_decomposition(A)
    print("L:")
    print(L)
    print("U:")
    print(U)


print("Ma trận Y là kết quả khi giải hệ LY=b")
Y=np.linalg.solve(L,b)
print(Y)
print("Ma trận X là kết quả khi giải hệ UX=Y")
X=np.linalg.solve(U,Y)
print(X)