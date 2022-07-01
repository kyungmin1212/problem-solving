from heapq import heappush,heappop

n,e=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

inf = int(1e9)

def dijkstra(start):
    distance = [inf for _ in range(n + 1)]
    heap=[]
    heappush(heap,(0,start))
    while heap:
        now_distance,node = heappop(heap)
        if distance[node]==inf:
            distance[node]=now_distance

        for next_node,weight in graph[node]:
            if distance[next_node]==inf:
                heappush(heap,(now_distance+weight,next_node))

    return distance

v_1,v_2=map(int,input().split())


start_1 = dijkstra(1)
start_n = dijkstra(n)
start_v1 = dijkstra(v_1)

start_1_end_v1 = start_1[v_1]
start_1_end_v2 = start_1[v_2]

start_n_end_v1 = start_n[v_1]
start_n_end_v2 = start_n[v_2]

start_v1_end_v2 = start_v1[v_2]

answer = min(start_1_end_v1+start_v1_end_v2+start_n_end_v2,start_1_end_v2+start_v1_end_v2+start_n_end_v1)
if answer>=inf:
    print(-1)
else:
    print(answer)
