import sys
from heapq import heappush,heappop

input=sys.stdin.readline

n,m=map(int,input().split())

graph=[]
backtest=[[] for _ in range(n+1)]
inf=int(1e9)
distance=[-inf for _ in range(n+1)]
path = [i for i in range(n+1)]
for _ in range(m):
    s,e,w=map(int,input().split())
    graph.append([s,e,w])
    backtest[e].append(s)

visited=[False for _ in range(n+1)]

def check_connect_lastnode():
    q=[]
    heappush(q,n)
    visited[n]=True
    while q:
        a=heappop(q)
        for front_node in backtest[a]:
            if not visited[front_node]:
                visited[front_node]=True
                heappush(q,front_node)

def bellmanford(start):
    distance[start] = 0
    path[start]=start
    for i in range(1,n+1):
        for j in range(m):
            start,end,weight=graph[j]
            if distance[start]!=-inf and distance[end]<distance[start]+weight:
                path[end]=start
                distance[end]=distance[start]+weight

                if i==n and visited[end]:
                    return True
    return False

check_connect_lastnode()
check = bellmanford(1)
if distance[-1]==-inf:
    print(-1)
elif check:
    print(-1)
else:
    result = [n]
    end = n
    while end != 1:
        end = path[end]
        result.append(end)
    print(*result[::-1])


