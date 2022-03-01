import sys
sys.setrecursionlimit(int(1e6))

n,m,k=map(int,input().split())

food_waste=[[0 for _ in range(m+2)] for _ in range(n+2)]
check_food_waste=[[0 for _ in range(m+2)] for _ in range(n+2)]
for _ in range(k):
    r,c=map(int,input().split())
    food_waste[r][c]=1

move=[(-1,0),(1,0),(0,-1),(0,1)]

def find_max(r,c):
    global value
    value+=1
    check_food_waste[r][c]=1

    for dy,dx in move:
        if food_waste[r+dy][c+dx]==1 and check_food_waste[r+dy][c+dx]==0:
            find_max(r+dy,c+dx)
    return

max_value=0
for row in range(1,n+1):
    for column in range(1,m+1):
        if food_waste[row][column]==1 and check_food_waste[row][column]==0:
            value = 0
            find_max(row,column)
            v=value
            if max_value<v:
                max_value=v

print(max_value)