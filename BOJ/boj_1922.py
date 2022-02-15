n=int(input())
m=int(input())
graph=[]
parent=[i for i in range(n+1)]
for _ in range(m):
    graph.append(list(map(int,input().split())))

graph.sort(key=lambda x:x[2])

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

cost=0
for i in range(m):
    a,b,c=graph[i]
    a=find(a)
    b=find(b)
    if a==b:
        continue
    else:
        union(a,b)
        cost+=c

print(cost)