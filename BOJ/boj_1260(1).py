from collections import deque

# dfs 는 재귀적으로 첫번째 것이 방문한적없으면 그 첫번째 자식노드로 들어가서 dfs 를 자시 재귀로 한다.
def dfs(v):
    if not(visited[v]):
        visited[v]=True
        print(v,end=" ")
        for e in adj[v]:
            dfs(e)

# bfs 는 deque 에다가 담는것 첫번째 것을 계속 빼내야 하기때문에
# q.popleft()를 이용하여 하나씩 거낸다 하나꺼낸것의 자식노드를 그 뒤에 이어서 계속 추가시킨다.
def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if not(visited[v]):
            print(v,end=" ")
            visited[v]=True
            for e in adj[v]:
                q.append(e)

n,m,v=list(map(int,input().split()))
adj=[[] for _ in range(n+1)]

# dfs bfs 를 할때는 연결된 노드를 모두 리스트 안에 저장해줘야한다 쌍방향으로
for _ in range(m):
    x,y=list(map(int,input().split()))
    adj[x].append(y)
    adj[y].append(x)

# 항상 작은거부터 꺼내야하므로 작은거 순으로 정렬을 해줘야한다.
for e in adj:
    e.sort()

# 방문했는지 안했는지 꼭 표시를 해줘야 한다. 안그러면 실행 불가
visited=[False]*(n+1)
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)


