n = int(input())
coord=[int(input()) for _ in range(2*n)]
def polygon(n,coord):
    side=[]
    for i in range(0,n+1,2):
        d=(((coord[i+1]-coord[i])**2+(coord[i+3]-coord[i+2])**2)**0.5)
        side.append(d)
    side.append(((coord[-1]-coord[-2])**2+(coord[1]-coord[0])**2)**0.5)
    return sum(side)
print(polygon(n,coord))

assert(polygon(3,[0,0,8,2,-2,6])== 24.0)
