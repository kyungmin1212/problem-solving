from collections import deque

n,m=map(int,input().split())

miro=[[0 for _ in range(m+2)]]

for _ in range(n):
    miro.append([0]+list(map(int,list(input())))+[0])

miro.append([0 for _ in range(m+2)])

move=[(-1,0),(1,0),(0,1),(0,-1)]
check_miro=[[0 for _ in range(m+2)] for _ in range(n+2)]

def bfs(r,c):
    check_miro[r][c]=1
    q=deque()
    q.append([1,r,c])
    while q:
        count,row,column=q.popleft()
        for dy,dx in move:
            if (row+dy)==n and (column+dx)==m:
                return count+1
            if miro[row+dy][column+dx]==1 and check_miro[row+dy][column+dx]==0:
                q.append([count+1,row+dy,column+dx])
                check_miro[row+dy][column+dx]=1

print(bfs(1,1))

