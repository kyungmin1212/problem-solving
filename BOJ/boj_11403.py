n=int(input())

inf=int(1e9)

map_list=[]

for _ in range(n):
    a=list(map(int,input().split()))
    map_list.append(a)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if k==i or k==j:
                continue
            if map_list[i][j]==1:
                continue
            else:
                if map_list[i][k]==1 and map_list[k][j]==1:
                    map_list[i][j]=1

for i in range(n):
    print(*map_list[i])
