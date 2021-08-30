sign = input()
n = int(input())
nums=[int(input()) for _ in range(n)]
if sign == '+':
    result = sum(nums)
elif sign == '*':
    result = 1
    for i in range(len(nums)):
        result *= nums[i]
print(result)  
