import math

n,m=map(int,input().split())

def find(x):
    if parent[x]==x:
        return x
    else:
        return find(parent[x])

def distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def union(a,b):
    x=find(a)
    y=find(b)
    if x!=y:
        if x<y:
            parent[y]=x
        else:
            parent[x]=y
infor=[]
edge=[]
parent={}

def checkparent(a,b):
    x=find(a)
    y=find(b)
    if x==y:
        return True
    else:
        return False

for _ in range(n):
    x,y=map(int,input().split())
    infor.append([x,y])

for i in range(n-1):
    for j in range(i+1,n):
        edge.append([i+1,j+1,distance(infor[i][0],infor[j][0],infor[i][1],infor[j][1])])

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

edge.sort(key=lambda x:x[2])
result=0
for x,y,dist in edge:
    if not(checkparent(x,y)):
        union(x,y)
        result+=dist
print(f"{result:.2f}")