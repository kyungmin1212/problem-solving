n,k=map(int,input().split())

coin_list=[]

for _ in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

count=0

for coin in coin_list:
    if k//coin>=1:
        count+=k//coin
        k%=coin

print(count)