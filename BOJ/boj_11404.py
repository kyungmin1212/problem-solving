n=int(input())
m=int(input())

inf=int(1e9)
short_map=[[inf for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    s,e,w=map(int,input().split())
    short_map[s][e]=min(short_map[s][e],w)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                continue
            if k==i or k==j:
                continue
            short_map[i][j]=min(short_map[i][j],short_map[i][k]+short_map[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if short_map[i][j]==inf:
            print(0,end=" ")
        else:
            print(short_map[i][j],end=" ")
    print()