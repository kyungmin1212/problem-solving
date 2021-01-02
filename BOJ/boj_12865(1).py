n,k=map(int,input().split())
# 리스트안에 리스트를 여러개 넣을때 유용한 방식 (k+1)x(n+1) 칸 만들때 사용하기 좋은것 같다 .
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight,value=map(int,input().split())
    for j in range(1,k+1):
        if j<weight:
            dp[i][j]=dp[i-1][j]
        # 넣을수 있는 가방 무게가 (j) weight보다 작을때는 그대로 내려오면 된다.
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
        # 넣을수 있는 가방 무게가 (j) weight보다 클때는 j에서 weight 만큼 뺀 만큼의 무게 의 가치에서
        # 가치를 더한만큼하고 비교해주면된다.
print(dp[n][k])