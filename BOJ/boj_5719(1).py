from collections import deque
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap=[]
    heapq.heappush(heap,(0,start))
    distance[start]=0
    while heap:
        dis,now=heapq.heappop(heap)
        # 일종의 방어 코드 밑에 for문에서 알아서 걸러주지만 한번 더써준것
        if distance[now]<dis:
            continue
        for e in adj[now]:
            cost=dis+e[1]
            if distance[e[0]]>cost and not(checked[now][e[0]]):
                distance[e[0]]=cost
                heapq.heappush(heap,(cost,e[0]))

def bfs(end):
    q=deque()
    q.append(end)
    while q:
        a=q.popleft()
        for i in reversed_adj[a]:
            if distance[a]==distance[i[0]]+i[1]:
                checked[i[0]][a]=True
                q.append(i[0])


while True:
    n,m=map(int,input().split())
    if n==0:
        break
    start,end=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    reversed_adj=[[] for _ in range(n+1)]
    for _ in range(m):
        x,y,cost=map(int,input().split())
        adj[x].append([y,cost])
        reversed_adj[y].append([x,cost])
    checked=[[False]*(n+1) for _ in range(n+1)]
    distance=[1e9]*(n+1)
    dijkstra(start)
    bfs(end)
    distance=[1e9]*(n+1)
    dijkstra(start)
    if distance[end]!=1e9:
        print(distance[end])
    else:
        print(-1)