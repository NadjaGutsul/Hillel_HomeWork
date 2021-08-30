import numpy as np
n=int(input())
num=np.zeros(n*n, dtype=np.int64).reshape(n, n)
for i in range(n):
    num[i][i]=1
print(num)
    