n=int(input())

house=[[0 for _ in range(n+2)]]

for _ in range(n):
    house.append([0]+list(map(int,list(input())))+[0])

house.append([0 for _ in range(n+2)])

check_house=[[0 for _ in range(n+2)] for _ in range(n+2)]

move=[(-1,0),(1,0),(0,1),(0,-1)]

def check(r,c):
    global count
    count+=1
    check_house[r][c]=1
    for dy,dx in move:
        if house[r+dy][c+dx]==1 and check_house[r+dy][c+dx]==0:
            check(r+dy,c+dx)
    return

answer_list=[]
total_count=0
for row in range(1,n+1):
    for column in range(1,n+1):
        count=0
        if house[row][column]==1 and check_house[row][column]==0:
            check(row,column)
            total_count+=1
            answer_list.append(count)

print(total_count)
answer_list.sort()
for answer in answer_list:
    print(answer)

