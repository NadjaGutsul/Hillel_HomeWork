n=int(input())
mat_a, mat_b=[[int(input()) for _ in range(n)] for _ in range(n)],[[int(input()) for _ in range(n)] for _ in range(n)]

def matrix(mat_a,mat_b):
    mat_c=[[0 for row in range(len(mat_a))] for col in range(len(mat_b[0]))]
    for i in range(len(mat_a)):
        for j in range(len(mat_b[0])):
            for k in range(len(mat_b)):
                mat_c[i][j] += mat_a[i][k]*mat_b[k][j]
    return mat_c
print(matrix(mat_a,mat_b))
