n,m=map(int,input().split())

inf=int(1e9)
distance=[inf for _ in range(n+1)]
graph=[]

for _ in range(m):
    s,e,w=map(int,input().split())
    graph.append([s,e,w])


def bellmanford(start):
    distance[start]=0
    for i in range(1,n+1):
        for j in range(m):
            start,end,weight=graph[j]
            if distance[start]!=inf and distance[end]>distance[start]+weight:
                distance[end]=distance[start]+weight
                if i==n:
                    return False
    return True



check=bellmanford(1)

if check:
    for i in range(2,len(distance)):
        if distance[i]==inf:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)