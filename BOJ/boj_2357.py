import math

n,m=map(int,input().split())

max_n=2**(math.ceil(math.log(n,2)))

inf = int(1e9)

segment_tree=[[inf,0] for _ in range(max_n*2)]

for i in range(n):
    value=int(input())
    segment_tree[max_n+i]=[value,value]

for i in reversed(range(max_n)):
    a = segment_tree[i*2]
    b = segment_tree[i*2+1]
    segment_tree[i][0]=min(a[0],b[0])
    segment_tree[i][1]=max(a[1],b[1])

def find_value(start,end,left,right,index):
    if start<=left and end>=right:
        return segment_tree[index]
    elif start>right or end<left:
        return [inf,0]
    else:
        l=find_value(start,end,left,(left+right)//2,index*2)
        r=find_value(start,end,(left+right)//2+1,right,index*2+1)
        return [min(l[0],r[0]),max(l[1],r[1])]

for _ in range(m):
    a,b=map(int,input().split())
    min_value,max_value=find_value(a-1,b-1,0,max_n-1,1)
    print(min_value,max_value)