N,L,I=map(int,input().split())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

dp[0][0]=1

for i in range(1,N+1):
    dp[i][0]=1
    for j in range(1,N+1):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        

answer=''
for i in reversed(range(N)):
    if I>sum(dp[i][:L+1]):
        answer+="1"
        I-=sum(dp[i][:L+1])
        L-=1
    else:
        answer+="0"

print(answer)