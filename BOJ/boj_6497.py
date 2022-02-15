def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def find(a):
    if a==parent[a]:
        return a
    return find(parent[a])

while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    graph=[]
    parent=[i for i in range(n)]
    total=0
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph.append([a,b,c])
        total+=c
    graph.sort(key=lambda x:x[2])

    count=0
    for i in range(m):
        a,b,c=graph[i]
        a=find(a)
        b=find(b)
        if a==b:
            continue
        else:
            union(a,b)
            count+=c

    print(total-count)