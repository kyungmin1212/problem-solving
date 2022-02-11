from collections import defaultdict
from heapq import heappop,heappush

V,E=map(int,input().split())
start=int(input())

graph=defaultdict(list)

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])

inf=int(1e9)
distance=[inf for _ in range(V+1)]

def dijkstra(start):
    q=[]
    heappush(q,(0,start))
    while q:
        now_distance,now_node=heappop(q)
        if distance[now_node]!=inf:
            continue
        else:
            distance[now_node]=now_distance

        for next_node,weight in graph[now_node]:
            if now_distance+weight>=distance[next_node]:
                continue
            else:
                heappush(q,(now_distance+weight,next_node))

dijkstra(start)
for i in range(1,len(distance)):
    if distance[i]==inf:
        print("INF")
    else:
        print(distance[i])

