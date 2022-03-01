from collections import deque

def find(f,r,c,max_f,max_r,max_c):
    check_building[f][r][c]=1
    q=deque()
    q.append([0,f,r,c])
    while q:

        count,floor,row,column=q.popleft()
        for dz,dy,dx in move:

            if floor+dz<0 or floor+dz>=max_f or row+dy<0 or row+dy>=max_r or column+dx<0 or column+dx>=max_c:
                continue
            if building[floor+dz][row+dy][column+dx]=="E":
                return count+1
            if building[floor+dz][row+dy][column+dx]=="." and check_building[floor+dz][row+dy][column+dx]==0:
                q.append([count+1,floor+dz,row+dy,column+dx])
                check_building[floor+dz][row+dy][column+dx]=1
    return False

while True:
    l,r,c=map(int,input().split())
    if l==0 and r==0 and c==0:
        break

    building=[]
    check_building=[[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for fl in range(l):
        floor=[]
        for ro in range(r):
            floor.append(list(input()))
            if "S" in floor[-1]:
                start_point=(fl,ro,floor[-1].index("S"))
        input()
        building.append(floor)

    move=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    s_f,s_r,s_c=start_point
    answer=find(s_f,s_r,s_c,l,r,c)
    if not answer:
        print("Trapped!")
    else:
        print(f'Escaped in {answer} minute(s).')


