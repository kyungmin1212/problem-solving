import sys
import math
input = sys.stdin.readline

n=int(input())

max_k=int(math.log(n,2))+1

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1 for _ in range(n+1)]
dp = [[0 for _ in range(n+1)] for _ in range(max_k+1)]

def init_dp_depth(node,now_depth):
    depth[node]=now_depth
    for next_node in graph[node]:
        if depth[next_node]==-1:
            dp[0][next_node]=node
            init_dp_depth(next_node,now_depth+1)

init_dp_depth(1,0)


# dp[row][column]=dp[row-1][dp[row-1][column]]으로 업데이트 하는 이유
# dp[row-1][column]값은 그 column 값에서 2^(row-1)만큼 올라간 지점을 의미하는것
# 그 올라간 지점의 값에서 2^(row-1)만큼 또 올라가게되면 최종적으로 column 에서 2^(row)만큼 올라간것이 됨
for row in range(1,max_k+1):
    for column in range(1,n+1):
        dp[row][column]=dp[row-1][dp[row-1][column]]

def find_lca_count(a,b):
    count=0
    if depth[a]>depth[b]:
        b,a=a,b

    for i in reversed(range(max_k+1)):
        if depth[b]-depth[a]>=(1<<i): # 2^i보다 크거나같게 차이난다면 그만큼 위로 올라가면됨
            b=dp[i][b]
            count+=(1<<i)

    if a==b:
        return count

    # 부모가 같을때까지 올라감
    for i in reversed(range(max_k+1)):
        if dp[i][a]!=dp[i][b]:
            a=dp[i][a]
            b=dp[i][b]
            count+=(1<<(i+1)) # a와 b 둘다 올라가기때문에 2를 한번 더 곱해준것

    return count+2 # 부모까지 올라가는 경우도 생각해야하기때문에 +2를 해줌


m=int(input())

start_point=int(input())
answer=depth[start_point]

for _ in range(m-1):
    end_point=int(input())
    answer+=find_lca_count(start_point,end_point)
    start_point=end_point
print(answer)