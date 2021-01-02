"""
문제 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
입력 : 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.
"""
from collections import deque

def dfs(v):
    print(v,end=" ")
    visited[v]=True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if not(visited[v]):
            visited[v]=True
            print(v,end=" ")
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n,m,v=map(int,input().split())
# adj 연결된 노드들을 만들어준다 .
adj=[[] for _ in range(n+1)]

# adj 연결된 노드들을 각각 정점에 대하여 그것을 추가시켜준다.
for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

# adj 에서 각각 연결된 노드들을 순서대로 정렬시켜준다.
for e in adj:
    e.sort()

visited=[False]*(n+1)
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)