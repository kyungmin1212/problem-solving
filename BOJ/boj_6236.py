n,m=map(int,input().split())

money_list=[]

for _ in range(n):
    money_list.append(int(input()))

start=max(money_list)
end=10000*100000

while start<=end:
    mid=(start+end)//2

    remain=mid
    count=1 # 처음에 한번 꺼내놓은 상태
    for money in money_list:
        if money<=remain:
            remain-=money
        else:
            count+=1
            remain=mid-money # 인출하고 돈을 사용해야함
    if count>m: # 돈이 너무 적은것
        start=mid+1
    else:
        answer=mid
        end=mid-1

print(answer)
