n = int(input())
nums=[int(input()) for _ in range(n)]
def only_ones(n,nums):
    ones=[]
    for i in range(n):
        if nums.count(nums[i])==1:
            ones.append(nums[i])
    return ones
print(*only_ones(n,nums))

assert(only_ones(4,[1,2,2,3])==([1,3]))