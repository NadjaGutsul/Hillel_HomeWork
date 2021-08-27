n = int(input())
a, b = 1, 1
num=[]
def fibonacci(n,a,b,num):
    for i in range(n):
      num.append(a)
      a, b = b, a + b
    return num
print(*fibonacci(n,a,b,num))

assert(fibonacci(3,1,1,[])==[1,1,2])