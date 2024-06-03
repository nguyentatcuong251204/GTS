import numpy as np
import pandas as pd


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print('{:20}'.format(element), end='')
        print()


def chon_1(A, n, danhdau):
    for i in range(n):
        for j in range(n):
            if (danhdau[i][j] == 0 and abs(A[i][j] == 1)):
                return True, i, j
    return False, 0, 0


def chon_max(A, n, danhdau):
    maxA = -9999999999999999999999
    pivot_i = 0
    pivot_j = 0
    for i in range(n):
        for j in range(n):
            if (danhdau[i][j] == 0 and A[i][j] > maxA):
                maxA = A[i][j]
                pivot_i = i
                pivot_j = j

    return maxA, pivot_i, pivot_j


def chuan_hoa(A, n):
    idex = np.arange(n)
    for i in range(n):
        for j in range(n):
            if (A[i][j] != 0 and A[i][j] > 0.0000001):

                idex[i] = j

    return idex


def GaussJordan(A, danhdau, n, id, E):
    id = id + 1
    if (id == n+1):
        return E
    check_1, pivot_i, pivot_j = chon_1(A, n, danhdau)
    if (check_1):
        pivot = A[pivot_i][pivot_j]
    else:
        pivot, pivot_i, pivot_j = chon_max(A, n, danhdau)

    for i in range(n):
        if (i != pivot_i):
            factor = A[i][pivot_j] / pivot
            for j in range(n):
                A[i][j] = A[i][j] - factor * A[pivot_i][j]
            for j in range(n):
                E[i][j] = E[i][j] - factor * E[pivot_i][j]

    for i in range(n):
        for j in range(n):
            if (i == pivot_i or j == pivot_j):
                danhdau[i][j] = 1

    print("-------------------------------------------------------------------------------")
    print("Chọn phần tử: ", pivot)
    print("Ma trận A bước {}: ".format(id))
    print_matrix(A)
    print("Ma trận E bước {}: ".format(id))
    print_matrix(E)
    print("Mảng đánh dấu bước {}: ".format(id))
    print(danhdau)

    return GaussJordan(A, danhdau, n, id, E)


def arrange_theo_chuan(A, B, n, ind):
    for i in range(n-1):
        for j in range(i, n):
            if (ind[i] > ind[j]):
                for k in range(n):
                    A[i][k], A[j][k] = A[j][k], A[i][k]
                for k in range(n):
                    B[i][k], B[j][k] = B[j][k], B[i][k]
                ind[i], ind[j] = ind[j], ind[i]

    for i in range(n):
        for j in range(n):
            B[i][j] = B[i][j] / A[i][i]
            A[i][j] = A[i][j] / A[i][i]

    return A, B, ind


def main():
    # A = np.array([[2., 0., 0.], [6., 1., 0.], [-8., 5., 3.]])
    # A = pd.read_excel(
    #     "C:/Users/DELL/Downloads/dataGK20222/matrixA.xlsx", sheet_name="Sheet1", header=None)
    A = np.array([[1,3,0],[4,0,9],[-4,-9, 13]])

    
    C = A.copy()
    id = 0
    n = A.shape[0]
    danhdau = np.zeros((n, n))

    print("Giải theo thư viện: ")
    print(np.linalg.inv(A))
    print('Ma trận A ban đầu: ')
    print_matrix(A)
    print("Mảng đánh dấu ban đầu: ")
    print(danhdau)
    E = np.eye(n)

    B = GaussJordan(A, danhdau, n, id, E)
    print("----------------------------Sau khi rút gọn--------------------------")
    ind = chuan_hoa(A, n)
    A, B, ind = arrange_theo_chuan(A, B, n, ind)

    print("----------------------------Ma trận nghịch đảo--------------------------")
    print_matrix(B)
    print("Kiểm tra lại: ")
    print_matrix(C @ B)


main()