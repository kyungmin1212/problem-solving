n=int(input())

weights=list(map(int,input().split()))
weights.insert(0,0)
graph=[[] for _ in range(n+1)]
answer_dp=[[0,0] for _ in range(n+1)]
answer_path=[[[],[]] for _ in range(n+1)]
visited=[False for _ in range(n+1)]


for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node]=True
    answer_dp[node][0]=weights[node]
    answer_path[node][0].append(node)
    for number in graph[node]:
        if not visited[number]:
            a,b=dfs(number)
            answer_dp[node][0]+=b
            answer_dp[node][1] += max(a, b)

            answer_path[node][0]+=answer_path[number][1]
            if a>=b:
                answer_path[node][1]+=answer_path[number][0]
            else:
                answer_path[node][1]+=answer_path[number][1]


    return answer_dp[node]

dfs(1)
if answer_dp[1][0]>=answer_dp[1][1]:
    print(answer_dp[1][0])
    path=answer_path[1][0]
    path.sort()
    print(*path)
else:
    print(answer_dp[1][1])
    path=answer_path[1][1]
    path.sort()
    print(*path)

