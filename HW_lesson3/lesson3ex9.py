n = int(input())
nums=[int(input()) for _ in range(n)]
def more_than_two(n, nums):
    mtt=[]
    for i in range(n-2):
        if nums[i]<nums[i+1]>nums[i+2]:
            mtt.append(nums[i+1])
    return mtt

print(*more_than_two(n, nums))
assert(more_than_two(6, [1, 3, 2, 4, 3, 5])==[3, 4])
