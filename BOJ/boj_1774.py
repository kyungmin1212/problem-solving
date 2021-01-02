"""
문제 : 황선자씨는 우주신과 교감을 할수 있는 채널러 이다.
하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다.
이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.
하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다.
이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은
그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.
우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다.
하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을  좋아하지 않는다.
왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.
또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과
황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.
이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다.
우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다.
새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.
입력 : 첫째 줄에 우주신들의 개수(N<=1,000) 이미 연결된 신들과의 통로의 개수(M<=1,000)가 주어진다.
두 번째 줄부터 N개의 줄에는 황선자를 포함하여 우주신들의 좌표가 (0<= X<=1,000,000), (0<=Y<=1,000,000)가 주어진다.
그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.
출력 : 첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라. 출력은 소수점 둘째짜리까지 출력하여라.
"""
import math
import sys
input=sys.stdin.readline

def get_distance(p1,p2):
    a=p1[0]-p2[0]
    b=p1[1]-p2[1]
    return math.sqrt((a*a)+(b*b))

# n의 꼭대기에 있는 parent를 찾는과정이다.
def get_parent(parent,n):
    if parent[n]==n:
        return n
    return get_parent(parent,parent[n])

# a와 b 를 각각 꼭대기 까지 간다음에 그 부모노드의 값이 작은쪽이 그것의 부모노드가 된다.
def union_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# a와 b 의 부모노드가 같은지 판별하는것 그두게의 부모노드가 같다면 True 반환
def find_parent(parent,a,b):
    a=get_parent(parent,a)
    b=get_parent(parent,b)
    if a==b:
        return True
    else:
        return False

edges=[]
parent={}
locations=[]
n,m=map(int,input().split())
# n: 우주신 개수 , m :이미 연결된 통로의 개수
for _ in range(n):
    # 좌표를 넣어준다.
    x,y=map(int,input().split())
    locations.append((x,y))

# 좌표의 개수 =n
length=len(locations)

# i가 0부터 n-2까지이다.
for i in range(length-1):
    # j 는 1부터 n-1 까지이다.
    for j in range(i+1,length):
        # 간선에 모든 간선간의 거리와 그 좌표를 각각 넣어준다. 0: 1 2 3 4 ..n-1 , 1:2,3,4,... n-1 ,,, n-2:n-1
        edges.append((i+1,j+1,get_distance(locations[i],locations[j])))

# 1부터 n 까지 자기자신을 부모라고 지정해둔다.
for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    a,b=map(int,input().split())
    # a와 b 중에서 더 작은 값이 부모노드가 된다.
    union_parent(parent,a,b)

# 거리가 짧은 순으로 정렬하여서 연결안되어있는 노드들중에서 짧은거부터 연결되도록 한다.
edges.sort(key=lambda data:data[2])

result=0
for a,b,cost in edges:
    # find_parent 가 True 면 a,b가 같은 부모를 가지고 있다는 것이다.
    # 두개의 부모가 다르다면 그 두개를 연결시켜준다.
    if not find_parent(parent,a,b):
        union_parent(parent,a,b)
        result+=cost

print(f"{result:.2f}")