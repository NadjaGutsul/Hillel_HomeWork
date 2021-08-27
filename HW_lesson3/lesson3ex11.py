n = int(input())
nums=[int(input()) for _ in range(n)]

a, b = int(input()),int(input())
while a!=0 and b!= 0:
    if a>b:
        print(nums[a:b:-1])
    else:
        print(nums[a:b])
    a, b = int(input()),int(input())
