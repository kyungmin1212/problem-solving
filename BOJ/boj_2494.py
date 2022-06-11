n=int(input())

number_1=list(map(int,list(input())))
number_2=list(map(int,list(input())))

inf=int(1e9)
dp=[[inf for _ in range(10)] for _ in range(n)]
dp_2=[[(10,10) for _ in range(10)] for _ in range(n)] # (어디서왔는지 ,현재나사를 몇번 돌렸는지 정보)


def spin(index,plus,way):
    new_number_1=(number_1[index]+plus)%10
    ori_number_2=number_2[index]

    if way==0: # 왼쪽으로 회전
        spin_time=ori_number_2-new_number_1
        if spin_time<0:
            spin_time+=10
    elif way==1: # 오른쪽으로 회전
        spin_time=new_number_1-ori_number_2
        if spin_time<0:
            spin_time+=10

    return spin_time

# 숫자나사1 (누적 왼쪽 회전횟수가 0임 , 즉 plus=0)
dp[0][0]=spin(0,0,1) # 오른쪽으로 회전하면 누적 왼쪽 회전횟수는 그대로 0
dp_2[0][0]=(10,-spin(0,0,1))

dp[0][spin(0,0,0)]=spin(0,0,0) # 왼쪽으로 회전하면 누적 왼쪽 회전횟수는 그만큼 늘어남
dp_2[0][spin(0,0,0)]=(10,spin(0,0,0))

for i in range(n): # 숫자나사2부터 숫자나사N까지 똑같이 시행
    for j in range(10): # 바로 전단계의 숫자나사값중 inf가 아니라면 모두 고려를 해줘야함 , j가 누적 왼쪽 회전 횟수
        if dp[i-1][j]==inf:
            continue

        # 오른쪽 회전
        if dp[i][j]>dp[i-1][j]+spin(i,j,1):
            dp[i][j]=dp[i-1][j]+spin(i,j,1)
            dp_2[i][j]=(j,-spin(i,j,1))
        # 왼쪽 회전
        if dp[i][(j+spin(i,j,0))%10]>dp[i-1][j]+spin(i,j,0):
            dp[i][(j+spin(i,j,0))%10]=dp[i-1][j]+spin(i,j,0)
            dp_2[i][(j+spin(i,j,0))%10]=(j,spin(i,j,0))

min_value=min(dp[-1])
print(min_value)
min_value_index=dp[-1].index(min_value)

answer_list=[]

a,b=dp_2[n-1][min_value_index]

num=n
while num!=1:
    answer_list.append((num,b))
    num-=1
    a,b=dp_2[num-1][a]
answer_list.append((1,b))
answer_list=answer_list[::-1]

for a,b in answer_list:
    print(a,b)