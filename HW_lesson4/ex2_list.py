n=int(input())
num=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    num[i][i] = 1
    print(*num[i])
    