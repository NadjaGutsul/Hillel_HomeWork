import numpy as np
n, m = int(input()), int(input())
a = np.array([int(input()) for _ in range(m*n)]).reshape(n, m)
print(a.sum(axis=0))