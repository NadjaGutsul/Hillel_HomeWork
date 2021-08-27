n, m = int(input()),int(input())
n_nums=[int(input()) for _ in range(n)]
m_nums=[int(input()) for _ in range(m)]
def in_both(n, m, n_nums, m_nums):
    both=[]
    if n>m:
        for i in range(n):
            if n_nums[i] in m_nums:
                both.append(n_nums[i])
    elif n<m:
        for j in range[m]:
            if m_nums[j] in n_nums:
                both.append(m_nums[j])
    return both
print(*in_both(n, m, n_nums, m_nums))

assert(in_both(5, 4, [1,2,3,4,5], [2,6,6,6])==[2])
