n=int(input())

check=[0]*(1000001)

check[1]=1
check[2]=2

for i in range(3,n+1):
    check[i]=(check[i-1]+check[i-2])%15746

print(check[n])