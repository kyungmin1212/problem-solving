n=int(input())
m=int(input())

parent=[i for i in range(n+1)]

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)

    if a==b:
        return
    elif a>b:
        parent[a]=b
    elif a<b:
        parent[b]=a

for i in range(1,n+1):
    row_list=[0]+list(map(int,input().split()))
    for j in range(1,n+1):
        if row_list[j]==1:
            union(i,j)

routine=list(map(int,input().split()))
if len(routine)==1:
    print("YES")
else:
    flag=True
    for i in range(1,len(routine)):
        a=routine[i-1]
        b=routine[i]
        a=find(a)
        b=find(b)
        if a!=b:
            print("NO")
            flag=False
            break
    if flag:
        print("YES")