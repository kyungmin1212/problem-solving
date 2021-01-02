class Node:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
        self.parent=-1

def in_order(node,level):
    global x
    if node.left!=-1:
        in_order(tree[node.left],level+1)
    level_min[level]=min(level_min[level],x)
    level_max[level]=max(level_max[level],x)
    x+=1
    if node.right!=-1:
        in_order(tree[node.right],level+1)


tree={}

n=int(input())
level_min=[n]
level_max=[0]
x=1
root=-1
# 기본적인 노드 생성
for i in range(1,n+1):
    tree[i]=Node(i)
    level_min.append(n)
    level_max.append(0)
    # tree[i] 가 객체명이라고 생각(self)

for i in range(n):
    node,left,right=list(map(int,input().split()))
    tree[node].left=left
    tree[node].right=right
    if left!=-1:
        tree[left].parent=node
    if right!=-1:
        tree[right].parent=node

# root 노드가 꼭  1이 아니므로 root 노드가 1인것을 꼭 찾아줘야한다.
for i in range(1,n+1):
    if tree[i].parent==-1:
        root=i


in_order(tree[root],1)
level=1
width=level_max[1]-level_min[1]+1
for i in range(2,n+1):
    level_width=level_max[i]-level_min[i]+1
    if level_width>width:
        level=i
        width=level_width
print(level,width)
