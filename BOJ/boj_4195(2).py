# 4195 union find로 푼 풀이
t=int(input())
def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x
        number[x]+=number[y]
# 꼬리 물기라고 생각 오른쪽것이 왼쪽거를 꼬리를 문다고 생각
# 기존 y 에 꼬리가 달려있으면 그것도 다가지고 x를 무는것이다.
# 여기서 x , y 는 자기가 가지고 있는 요소들중에 제일 머리쪽으로 이동해야한다. 머리로 무는거니까
# 머리에는 꼬리가 여러개가 달릴수도 있다 여러곳이 물수도 있으니까
for _ in range(t):
    f=int(input())
    parent={}
    number={}

    for _ in range(f):
        x,y=input().split()
        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1
        union(x,y)
        print(number[find(x)])