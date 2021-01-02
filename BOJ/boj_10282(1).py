# 다익스타리의 개념 시작점에서 각 노드까지의 거리들을 지정하는거다
# 각 거리들을 1e9 로 거대하게 잡아놓는다 그러고나서 cost 가 더 작을경우 그걸로 업데이트 시킨다.
# 최단경로를 구하는것이기때문에 작을겨우 업데이트
# 항상 start 값을 넣어줄때 distance[start]=0 으로 세팅해준다.
# heap=[] 을 만들고 heap 에다가 heapq.heappush(heap,(0,start))를 넣어준다.
# while heap: 힙에 데이터가 있으면 계속 반복한다.
# dis,now 현재까지 거리와 현재 지점을 heapq.heappop(heap)을 통하여 꺼낸다.
# heapq를 통해 꺼내기때문에 현재까지 거리가 짧은거 부터 꺼내지게 된다.
# 이렇게 하는이유는 시간을 절약하기 위해서이다 만약에 distance[now] 지금까지 거리보다
# 꺼낸 dis 가 크다면 굳이 밑에 동작을 수행할필요가 없다. 넘어가면된다.
# 그후 현재 지점에서 인접된 노드들을 for i in adj[now] 를 통하여 꺼내준다.
# 다음지점까지의 거리는 지금까지의 거리 dis 에다가 근접한 지점까지의 거리i[1]을 더해주면된다.
# 그후 cost가 distance[다음지점]보다 작다면 cost 를 업데이트 시켜주면 된다.
# 그리고 나서 그 다음지점을 heap 에다가 넣어줘야 한다. 그다음지점에서 또 체크를 해야하기 때문에에
import heapq

t=int(input())

def dijkstra(start):
    heap=[]
    heapq.heappush(heap,(0,start))
    distance[start]=0
    while heap:
        dis,now=heapq.heappop(heap)
        if dis>distance[now]:
            continue
        for i in adj[now]:
            cost=dis+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(heap,(cost,i[0]))

for _ in range(t):
    n,d,start=map(int,input().split())
    adj=[[] for _ in range(n+1)]
    distance=[1e9]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        adj[b].append([a,s])
    dijkstra(start)
    count=0
    max_value=0
    for i in distance:
        if i!=1e9:
            count+=1
            if i>max_value:
                max_value=i
    print(count,max_value)