"""
문제 : 이진트리를 다음의 규칙에 따라 행과 열에 번호가 붙어있는 격자 모양의 틀 속에 그리려고 한다.
이때 다음의 규칙에 따라 그리려고 한다.
이진트리에서 같은 레벨(level)에 있는 노드는 같은 행에 위치한다.
한 열에는 한 노드만 존재한다.
임의의 노드의 왼쪽 부트리(left subtree)에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고,
오른쪽 부트리(right subtree)에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.
노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.
이와 같은 규칙에 따라 이진트리를 그릴 때 각 레벨의 너비는 그 레벨에 할당된 노드 중
가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다.
트리의 레벨은 가장 위쪽에 있는 루트 노드가 1이고 아래로 1씩 증가한다.
아래 그림은 어떤 이진트리를 위의 규칙에 따라 그려 본 것이다.
첫 번째 레벨의 너비는 1, 두 번째 레벨의 너비는 13, 3번째, 4번째 레벨의 너비는 각각 18이고,
5번째 레벨의 너비는 13이며, 그리고 6번째 레벨의 너비는 12이다.
그림 2250 참고
우리는 주어진 이진트리를 위의 규칙에 따라 그릴 때에 너비가 가장 넓은 레벨과 그 레벨의 너비를 계산하려고 한다.
위의 그림의 예에서 너비가 가장 넓은 레벨은 3번째와 4번째로 그 너비는 18이다.
너비가 가장 넓은 레벨이 두 개 이상 있을 때는 번호가 작은 레벨을 답으로 한다.
그러므로 이 예에 대한 답은 레벨은 3이고, 너비는 18이다.
임의의 이진트리가 입력으로 주어질 때 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 프로그램을 작성하시오
입력 : 첫째 줄에 노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)이 주어진다.
다음 N개의 줄에는 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호가 순서대로 주어진다.
노드들의 번호는 1부터 N까지이며, 자식이 없는 경우에는 자식 노드의 번호에 -1이 주어진다.
출력 : 첫째 줄에 너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력한다.
너비가 가장 넓은 레벨이 두 개 이상 있을 때에는 번호가 작은 레벨을 출력한다.
"""
class Node:
    def __init__(self,number):
        self.parent=-1
        self.number=number
        self.left_node=None
        self.right_node=None
# 이렇게만 만들고 각 노드에 대해서 그 노드점에 대한 number값들만 우선 입력한다
# 그형식을 tree[number]=Node(number) 이런식으로 딕셔너리 형태로 생성한다 tree={}
# 여기서 tree[number] 형태로 해주는 이유는 for 문안에서 돌때 number을 각각 입력시키는 tree_number 이런식으로 할수는 없기때문에
# 딕셔너리 형태를 이용해서 그 주어진 값에 따라 변수를 다르게 지정한다.
# 즉 딕셔너리를 이용하는경우는 for 문안에서 도는 변수에 따라 변수명을 달리 사용하고 싶을때 사용한다.
# 그리고 나중에 left랑 right 랑 parent 를 각각 지정해주면된다


# 중외선회를 생각하자 제일왼쪽으로갈때까지는 x 가 증가하지 않다가 제일 왼쪽으로 가고 그 level에서 min과 max 를 지정하고
# 그다음에 밖으로 빠져나오게되면 x는 2가되게 되고 한단계낮은 level 에서의 min과 max 값이 지정하고 x는 3이된다.
# 그다음에 오른쪽 노드가 있다면 오른쪽 노드로 가게 되는데 오른쪽 노드는 다시 level 을 1증가시키고 그때의 level min과 max 를 지정하게 된다.
# 그다음에 다시 x는 4가 되게 된다.
# 최종적으로 생각해보면 왼쪽 아래부터 차근차근 지정한다고 생각하기

def in_order(node,level):
    global level_depth,x
    level_depth=max(level_depth,level)
# 왼쪽 노드가 있으면 계속 쭉 내려간다 .
    if node.left_node!=-1:
        in_order(tree[node.left_node],level+1)
# 왼쪽노드 끝나는 지점에 온경우 이때 level 이 제일 낮은 쪽(값이 높은층)이 된다.

# 처음에 level_min=[n,n,n,....,n] 으로 설정하였기 때문에 min 값은 x 가 된다.
    level_min[level]=min(level_min[level],x)
# 처음에 level_max=[0,0,0,...,0] 으로 설정하였기 때문에 max 값은 x 가 된다.
    level_max[level]=max(level_max[level],x)
# x에 1을 더해주게된다. 한단계 내려간다는것
    x+=1
# 오른쪽 노드가 계속 있다면 그쪽으로 쭉 내려간다. 내려가다가 다시 왼쪽ㅇ ㅣ있으면 그 왼쪽으로 쭉내려가고 나서 오른쪽으로 가는것
    if node.right_node!=-1:
        in_order(tree[node.right_node],level+1)
# 결과적으로 level_depth 가 업데이트 되고 level_max 랑 leve_min 값이 각각의 level 에 대하여 업데이트 되게 된다.

n=int(input())
tree={}
level_min=[n]
level_max=[0]
root=-1
x=1
level_depth=1

for i in range(1,n+1):
    tree[i]=Node(i)
    # 각각 1노드 부터 n 노드까지 각각 노드점만 생성한다(아직 left ,right , parent 가 지정이 안되어 있는 상태이다.)
    level_min.append(n)
    # level_min 에다가 각각 n을 n번만큼 추가 시켜준다.
    level_max.append(0)
    # level_max 에다가 각각 0을 n번만큼 추가 시켜준다.

for _ in range(n):
    number,left_node,right_node=map(int,input().split())
    # 각각 생성된 노드객체에다가 left right 를 지정해준다.
    tree[number].left_node=left_node
    tree[number].right_node=right_node
    # left 가 있을경우 그 tree[left_node] 에 대한 부모를 number 로 지정해준다.
    if left_node!=-1:
        tree[left_node].parent=number
    # right 가 있을경우 그 tree[right_node] 에 대한 부모를 number로 지정해준다.
    if right_node!=-1:
        tree[right_node].parent=number

# 처음 시작하는 노드를 잡기위하여 1부터 n 까지 그 tree의 노드들을 돌면서 부모노드가 -1 인 꼭대기 노드를 찾는다.
for i in range(1,n+1):
    if tree[i].parent==-1:
        root=i

# root 가 1인 경우이기 때문에  node 변수에다가 tree[1]을 넣어주고 level 에다가 1층이므로 1을 넣어준다 .
in_order(tree[root],1)

# def in_order(node,level):
#     global level_depth,x
#     level_depth=max(level_depth,level)
## 왼쪽 노드가 있으면 계속 쭉 내려간다 .
#     if node.left_node!=-1:
#         in_order(tree[node.left_node],level+1)
## 왼쪽노드 끝나는 지점에 온경우 이때 level 이 제일 낮은 쪽(값이 높은층)이 된다.

## 처음에 level_min=[n,n,n,....,n] 으로 설정하였기 때문에 min 값은 x 가 된다.
#     level_min[level]=min(level_min[level],x)
## 처음에 level_max=[0,0,0,...,0] 으로 설정하였기 때문에 max 값은 x 가 된다.
#     level_max[level]=max(level_max[level],x)
## x에 1을 더해주게된다. 한단계 내려간다는것
#     x+=1
## 오른쪽 노드가 계속 있다면 그쪽으로 쭉 내려간다. 내려가다가 다시 왼쪽ㅇ ㅣ있으면 그 왼쪽으로 쭉내려가고 나서 오른쪽으로 가는것
#     if node.right_node!=-1:
#         in_order(tree[node.right_node],level+1)
## 결과적으로 level_depth 가 업데이트 되고 level_max 랑 leve_min 값이 각각의 level 에 대하여 업데이트 되게 된다.
result_level=1
result_width=level_max[1]-level_min[1]+1
for i in range(2,level_depth+1):
    width=level_max[i]-level_min[i]+1
    if result_width<width:
        result_level=i
        result_width=width

print(result_level,result_width)


