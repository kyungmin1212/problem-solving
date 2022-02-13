from collections import defaultdict
from heapq import heappush,heappop

V=int(input())
E=int(input())

inf=int(1e9)
graph=defaultdict(list)
distance=[inf for _ in range(V+1)]

for _ in range(E):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

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

start,end=map(int,input().split())
dijkstra(start)
print(distance[end])
