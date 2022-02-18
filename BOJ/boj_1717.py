import sys

sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

n,m=map(int,input().split())

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
    if a>b:
        parent[a]=b
    elif a<b:
        parent[b]=a


for _ in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        union(b,c)
    elif a==1:
        b=find(b)
        c=find(c)
        if b==c:
            print("YES")
        else:
            print("NO")
