import math

n,m,k=map(int,input().split())

max_n= 2**math.ceil(math.log(n,2))

segment_tree=[1]*(max_n*2)

for i in range(n):
    segment_tree[max_n+i]=int(input())

for i in reversed(range(1,max_n)):
    segment_tree[i]=((segment_tree[2*i]%1000000007)*(segment_tree[2*i+1]%1000000007))%1000000007

def update_segement_tree(index,value):
    index=max_n+index-1
    segment_tree[index]=value
    while index//2>=1:
        index=index//2
        segment_tree[index]=((segment_tree[2*index]%1000000007)*(segment_tree[2*index+1]%1000000007))%1000000007

def find_segment_tree(start,end,left,right,index):
    if start<=left and end>=right:
        return segment_tree[index]
    elif start>right or end<left:
        return 1
    else:
        return find_segment_tree(start,end,left,(left+right)//2,index*2)*find_segment_tree(start,end,(left+right)//2+1,right,index*2+1)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update_segement_tree(b,c)
    else:
        print(find_segment_tree(b-1,c-1,0,max_n-1,1)%1000000007)