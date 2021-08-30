n, m = int(input()), int(input())
num=[[int(input()) for _ in range(m)] for _ in range(n)]
def summa(n, m, num):
    num_sum=[num[0][i]+num[1][i] for i in range(m)]
    return num_sum

print(summa(n,m,num))

assert(summa(2, 3, [[1,2.3],[4,5,6]])==[5,7,9])