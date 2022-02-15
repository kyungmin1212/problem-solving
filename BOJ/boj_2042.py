import math

n,m,k=map(int,input().split())
max_n=2**math.ceil(math.log(n,2))
segment_tree=[0 for _ in range(max_n*2)]

for i in range(n):
    segment_tree[max_n+i]=int(input())

for i in reversed(range(1,max_n)):
    segment_tree[i]=segment_tree[i*2]+segment_tree[i*2+1]

def update_segment_tree(index,value):
    index = max_n + index -1
    segment_tree[index]=value
    while index//2>=1:
        index=index//2
        segment_tree[index]=segment_tree[index*2]+segment_tree[index*2+1]

def find_segment_tree(start,end,left,right,index):
    if start<=left and right<=end:
        return segment_tree[index]
    elif left>end or right<start:
        return 0
    elif start>left or right>end:
        return find_segment_tree(start,end,left,(left+right)//2,index*2)+find_segment_tree(start,end,(left+right)//2+1,right,index*2+1)

for i in range(m+k):

    a,b,c=map(int,input().split())
    if a==1:
        update_segment_tree(b,c)
    elif a==2:
        print(find_segment_tree(b-1,c-1,0,max_n-1,1))
