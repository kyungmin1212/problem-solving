import math
import sys

sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline
n=int(input())

graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

depth=[-1 for _ in range(n+1)]
dp=[[[0,0] for _ in range(n+1)]]

def find_depth(start,now_depth):
    depth[start]=now_depth
    for next_node,weight in graph[start]:
        if depth[next_node]==-1:
            dp[0][next_node][0]=start
            dp[0][next_node][1]=weight
            find_depth(next_node,now_depth+1)

find_depth(1,0)

max_depth=max(depth)
max_k=int(math.log(max_depth,2))

for _ in range(max_k+1):
    dp.append([[0,0] for _ in range(n+1)])

for row in range(1,max_k+1):
    for column in range(1,n+1):
        dp[row][column][0]=dp[row-1][dp[row-1][column][0]][0]
        dp[row][column][1]=dp[row-1][dp[row-1][column][0]][1]+dp[row-1][column][1]


def find_LCA_distance(a,b):
    if depth[a]>depth[b]:
        b,a=a,b

    distance=0
    for i in reversed(range(max_k+1)):
        if depth[b]-depth[a]>=2**i:
            distance += dp[i][b][1]
            b=dp[i][b][0]

    if a==b:
        return distance

    while dp[0][a][0]!=dp[0][b][0]:
        for i in range(1,max_k+2):
            if dp[i][a][0]==dp[i][b][0]:
                distance += dp[i - 1][a][1]
                distance += dp[i - 1][b][1]

                a=dp[i-1][a][0]
                b=dp[i-1][b][0]

                break

    return distance+dp[0][a][1]+dp[0][b][1]

m=int(input())

for _ in range(m):
    a,b=map(int,input().split())
    print(find_LCA_distance(a,b))

