import math
import sys

sys.setrecursionlimit(int(1e5))

n=int(input())
# n개 노드가 1열로 연결된 트리라고 생각했을때 최대 깊이는 2^(max_k)가 된다고 생각하자.
# 예를 들어 8개면 최대 깊이는 7이 될것이다.(k=2까지 고려) 9개면 최대 깊이는 8이 될것이다.(k=3까지 고려)
# 사실 n-1 대신에 그냥 40000을 넣어도 된다.
# log값이기 때문에 dp가 그렇게 커질일이 없기다. 딱히 상관은 없지만 최적화를 하기 위하여 n-1로 넣어주었다.
max_k=math.floor(math.log(n-1,2))

graph=[[] for _ in range(n+1)]

# +2을 해주는 이유는 제일 마지막 parent_dp 행을 모두 0으로 초기화된 행을 만들기 위함이다.
parent_dp=[[[0,0] for _ in range(n+1)] for _ in range(max_k+2)]

# 각 노드의 depth 정보를 알아야지 얼만큼 올라가야하는지 알 수 있다.
depth=[-1 for _ in range(n+1)]

# graph 생성
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

# parent_dp 초기화 , depth 값 채우기
def make_dp_depth(start,depth_value):
    depth[start]=depth_value
    for node,weight in graph[start]:
        if depth[node]==-1:
            parent_dp[0][node][0]=start
            parent_dp[0][node][1]=weight
            make_dp_depth(node,depth_value+1)

make_dp_depth(1,0)

# parent_dp 값 업데이트
for i in range(1,max_k+1):
    for j in range(1,n+1):
        parent_dp[i][j][0]=parent_dp[i-1][parent_dp[i-1][j][0]][0]
        parent_dp[i][j][1]=parent_dp[i-1][parent_dp[i-1][j][0]][1]+parent_dp[i-1][j][1]

def find_lca(a,b):
    # b값을 더 큰 값으로 정해준다.
    if depth[a]>depth[b]:
        a,b=b,a

    for i in reversed(range(max_k+1)):
        if depth[b]-depth[a]>=2**i:
            b=parent_dp[i][b][0]

    if a==b:
        return a

    while parent_dp[0][a][0]!=parent_dp[0][b][0]:
        for i in range(1,max_k+2):
            if parent_dp[i][a][0]==parent_dp[i][b][0]:
                a = parent_dp[i - 1][a][0]
                b = parent_dp[i - 1][b][0]
                break

    return parent_dp[0][a][0]

def find_distance(a,b,lca):
    a_count=0
    for i in reversed(range(max_k+1)):
        if depth[a]-depth[lca]>=2**i:
            a_count+=parent_dp[i][a][1]
            a=parent_dp[i][a][0]

    b_count=0
    for i in reversed(range(max_k+1)):
        if depth[b]-depth[lca]>=2**i:
            b_count+=parent_dp[i][b][1]
            b=parent_dp[i][b][0]

    return a_count+b_count

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(find_distance(a,b,find_lca(a,b)))