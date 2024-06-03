import math
import numpy as np
import pandas as pd
def MakelablesFalse(labels,i,j):
	labels[i]=[False for k in range(len(labels[i]))]
	for i in range(len(labels)):
		labels[i][j]=False

def MaxInMatrix(a,labels):
	n=len(a)
	maxValue=-math.inf
	maxPos=None
	for i in range(n):
		for j in range(n):
			if labels[i][j]==True and abs(a[i][j])>maxValue:
				maxValue=abs(a[i][j])
				maxPos=(i,j)
	return maxValue,maxPos

def checkPriorPos(a,labels):
	priorPos=None
	n=len(a)
	for i in range(n):
			breakFlag=False
			for j in range(n):
				if labels[i][j]==True and (a[i][j]==1 or a[i][j]==-1):
					priorPos=(i,j)
					breakFlag=True
					break
			if breakFlag==True:break
	return priorPos
def print_matrix(a):
	for i in range(len(a)):
		print(a[i])

def main():
	# a=[	[1,6,5,10,-3],
	# 	[-9,1,-10,5,5],
	# 	[1,3,48,8,2],
	# 	[-10,6,-10,1,2],
	# 	[17,-8,4,3,-6]
	# 	]

	# b=[10,20,20,10,10]
	file=open("D:\giai_tich_so\input_gauss.txt")
	matrix=[line.split() for line in file]
	matrix=np.array(matrix)
	# print(matrix)
	A=np.zeros((matrix.shape[0],matrix.shape[1]))

	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			A[i][j]=float(matrix[i][j])
	a=A[:,:-1]
	b=A[:,-1]
	n=len(b)
	print("Ma trận a:")
	print(a)
	print("Ma trận b:")
	print(b)
	x=[None for i in range(n)]
	labels=[[True for i in range(n)] for i in range(n)]
	
	for k in range(n):
		priorPos=checkPriorPos(a,labels)
		maxValue,maxPos=MaxInMatrix(a,labels)		
		if priorPos==None:
			priorPos=maxPos
		keyrow=priorPos[0]
		keycol=priorPos[1]
		print("VỊ TRÍ PHẦN TỬ KHỬ : ")
		print((keyrow,keycol))
		print("Giá trị max",maxValue)
		MakelablesFalse(labels,keyrow,keycol)
		pivot=a[keyrow][keycol]
		for j in range(n):
			a[keyrow][j]=a[keyrow][j]/pivot
		print("MA TRẬN A SAU KHI CHUẨN HÓA HÀNG KHỬ ")
		print_matrix(a)
		b[keyrow]=b[keyrow]/pivot
		print("MA TRẬN B SAU KHI CHUẨN HÓA ")
		print_matrix(b)
		for i in range(n):
			if i==keyrow:continue
			factor=a[i][keycol]
			for j in range(n):
				a[i][j]-=factor*a[keyrow][j]
			b[i]=b[i]-factor*b[keyrow]
		print("MA TRẬN A SAU KHI BIẾN ĐỔI ")
		print_matrix(a)
		print("MA TRẬN B SAU KHI BIẾN ĐỔI ")
		print_matrix(b)
		print("------------------------------------")
	print("KẾT QUẢ ")
	print_matrix(a)
	print(b)
	for i in range(n):
		for j in range(n):
			if a[i][j]==1:
				x[j]=b[i]
	print("solutions: ",x)
main()