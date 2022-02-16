import math
import sys

sys.setrecursionlimit(int(1e5))

input = sys.stdin.readline

n=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth=[-1 for _ in range(n+1)]

dp=[[0]*(n+1)] # parent

def make_dp_depth(start,depth_value):
    depth[start]=depth_value
    for node in graph[start]:
        if depth[node]==-1:
            dp[0][node]=start
            make_dp_depth(node,depth_value+1)

make_dp_depth(1,0)

max_k=int(math.log(max(depth),2))
for _ in range(max_k+1):
    dp.append([0]*(n+1))

for i in range(1,max_k+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i-1][dp[i-1][j]]

def find_lca(a,b):
    # b가 크게 설정
    if depth[a] > depth[b]:
        a, b = b, a

    # max_k 는 해봤자 log 값이기 때문에 n이 100만이라고 해도 최대 20정도 밖에 되지 않는다. 따라서 모든 범위를 체크해줘도 된다.
    for i in reversed(range(max_k+1)):
        # depth[b]-depth[a] >=(1<<i) 인거랑 같은말이다
        if depth[b]-depth[a] >=2**i:
            b=dp[i][b]

    if a==b:
        return a


    while dp[0][a]!=dp[0][b]: # 같은 층에 있는데 만약 바로 위에 있는 (k=0 일때) 부모 노드가 같다면 멈추면된다.-> 그 부모노드가 LCA가 된다.
        for i in range(1,max_k+2):
            if dp[i][a]==dp[i][b]:
                a=dp[i-1][a]
                b=dp[i-1][b]
                break

    return dp[0][a]

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(find_lca(a, b))