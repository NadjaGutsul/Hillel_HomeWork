n = int(input())
nums=[int(input()) for _ in range(n)]
def ratio(n, nums):
    average=sum(nums)/len(nums)
    for i in range(len(nums)):
        if nums[i]>average:
            result = (f'{nums[i]} is greater than the arithmetic mean of this list')
        elif nums[i]<average:
            result = (f'{nums[i]} is less than the arithmetic mean of this list')
        elif nums[i]==average:
            result = (f'{nums[i]} is equal to the arithmetic mean of this list')
        print(result)
ratio(n, nums)
