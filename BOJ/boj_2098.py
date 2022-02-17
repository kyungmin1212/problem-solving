import sys
input=sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

inf=int(1e9)
dp=[[inf]*(2**(n)) for _ in range(n)]

def dfs(now,bit):
    if bit==(1<<(n))-1:
        if graph[now][0]!=0:
            return graph[now][0]
        else:
            return inf # 경로가 없기 때문에 무한대로 리턴해줘야지나중에 min에서 이 값을 포함시키지 않을것이다.

    if dp[now][bit]!=inf:
        return dp[now][bit]

    for i in range(1,n):
        if graph[now][i]!=0 and not (bit&(1<<i)):
            dp[now][bit]=min(dp[now][bit],dfs(i,bit|1<<i)+graph[now][i])

    return dp[now][bit]

print(dfs(0,1))