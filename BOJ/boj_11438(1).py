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
dp=[[0 for _ in range(n+1)]]

# 먼저 최대 깊이와 바로 위 부모노드를 dp 에 저장시켜준다.

def find_depth(node,now_depth):
    depth[node]=now_depth
    for next_node in graph[node]:
        if depth[next_node]==-1:
            dp[0][next_node]=node
            find_depth(next_node,now_depth+1)

find_depth(1,0)
max_depth=max(depth)

max_k=int(math.log(max_depth,2))
# max_k만큼 dp의 row 추가
for _ in range(max_k+1):
    dp.append([0 for _ in range(n+1)])

for row in range(1,max_k+1):
    for column in range(1,n+1):
        dp[row][column]=dp[row-1][dp[row-1][column]]

def find_LCA(a,b):
    # b가 더 깊이 있는 것으로 설정
    if depth[a]>depth[b]:
        b,a=a,b

    # 깊이 같게 설정해주기
    while depth[b]!=depth[a]:
        for i in reversed(range(max_k+1)):
            if depth[b]-depth[a]>=2**i:
                b=dp[i][b]
                break

    if a==b:
        return a

    # 같은 층에 있으므로 부모노드가 같아질때까지 같은 층수만큼 올라가기
    while dp[0][a]!=dp[0][b]: # 바로 위 부모노드가 같으면 그거 return 하면 됨
        for i in range(1,max_k+2): # max_k+2인게 중요!! max_k+1에서 값이 0 이 들어있어 같은 경우를 마지노선으로 해야하므로
            # 같은 층에 있는데 2**i만큼 올라간 경우 그 값이 같다면 그 2**(i-1)만큼만 올라감
            # 2**i 만큼올라가면 더 많이 올라가버려서 LCA가 아닌 그 더 윗단계의 부모노드가 구해질수 있음
            if dp[i][a]==dp[i][b]:
                a=dp[i-1][a]
                b=dp[i-1][b]
                break
    return dp[0][a]

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(find_LCA(a,b))