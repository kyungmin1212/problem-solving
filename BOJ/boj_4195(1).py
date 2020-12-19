# Union-Find 알고리즘
parent=[]
def find(x):
    # 가르키는 숫자랑 자기자신 하고 같아질때까지 진행
    if x==parent[x]:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    # find로 제일 부모에 있는거를 찾아간다.
    parent[y]=x

for i in range(0,5):
    parent.append(i)

union(1,4)
print(parent)
# 4 가 1을 가르키게 하고
union(2,4)
print(parent)
# 4가 가르키는 1이 2를 가르키게 한다.

for i in range(1,len(parent)):
    print(find(i),end=" ")
# 1은 2를 가르키고 2는 원래 2를 가르키고 3은 원래 3을 가르키고 4는 1을 가르키고 그 1이 2를 가르키므로 2