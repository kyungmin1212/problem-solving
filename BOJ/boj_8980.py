"""
문제 : 아래 그림과 같이 직선 도로상에 왼쪽부터 오른쪽으로 1번부터 차례대로 번호가 붙여진 마을들이 있다.
마을에 있는 물건을 배송하기 위한 트럭 한 대가 있고, 트럭이 있는 본부는 1번 마을 왼쪽에 있다.
이 트럭은 본부에서 출발하여 1번 마을부터 마지막 마을까지 오른쪽으로 가면서 마을에 있는 물건을 배송한다.
각 마을은 배송할 물건들을 박스에 넣어 보내며, 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
박스들은 모두 크기가 같다. 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 있다.
이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송하려고 한다.

조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
조건 3: 박스들 중 일부만 배송할 수도 있다.
마을의 개수, 트럭의 용량, 박스 정보(보내는 마을 번호, 받는 마을번호, 박스 개수)가 주어질 때, 트럭 한 대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오. 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.

예를 들어, 트럭 용량이 40이고 보내는 박스들이 다음 표와 같다고 하자.
보내는 마을	받는 마을	박스 개수
1	2	10
1	3	20
1	4	30
2	3	10
2	4	20
3	4	20
이들 박스에 대하여 다음과 같이 배송하는 방법을 고려해 보자.

(1) 1번 마을에 도착하면

다음과 같이 박스들을 트럭에 싣는다. (1번 마을에서 4번 마을로 보내는 박스는 30개 중 10개를 싣는다.)

보내는 마을	받는 마을	박스 개수
1	2	10
1	3	20
1	4	10
(2) 2번 마을에 도착하면

트럭에 실려진 박스들 중 받는 마을번호가 2인 박스 10개를 내려 배송한다. (이때 트럭에 남아있는 박스는 30개가 된다.)

그리고 다음과 같이 박스들을 싣는다. (이때 트럭에 실려 있는 박스는 40개가 된다.)

보내는 마을	받는 마을	박스 개수
2	3	10
(3) 3번 마을에 도착하면

트럭에 실려진 박스들 중 받는 마을번호가 3인 박스 30개를 내려 배송한다. (이때 트럭에 남아있는 박스는 10개가 된다.)

그리고 다음과 같이 박스들을 싣는다. (이때 트럭에 실려 있는 박스는 30개가 된다.)

보내는 마을	받는 마을	박스 개수
3	4	20
(4) 4번 마을에 도착하면

받는 마을번호가 4인 박스 30개를 내려 배송한다

위와 같이 배송하면 배송한 전체 박스는 70개이다. 이는 배송할 수 있는 최대 박스 개수이다.
입력 : 입력의 첫 줄은 마을 수 N과 트럭의 용량 C가 빈칸을 사이에 두고 주어진다.
N은 2이상 2,000이하 정수이고, C는 1이상 10,000이하 정수이다. 다음 줄에, 보내는 박스 정보의 개수 M이 주어진다.
M은 1이상 10,000이하 정수이다. 다음 M개의 각 줄에 박스를 보내는 마을번호, 박스를 받는 마을번호,
보내는 박스 개수(1이상 10,000이하 정수)를 나타내는 양의 정수가 빈칸을 사이에 두고 주어진다.
박스를 받는 마을번호는 보내는 마을번호보다 크다.
출력 : 트럭 한 대로 배송할 수 있는 최대 박스 수를 한 줄에 출력한다.
"""
import sys
n,c=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
arr=[]
for i in range(m):
    a=list(map(int,sys.stdin.readline().split()))
    arr.append(a)

for i in range(len(arr)):
    arr[i].append(arr[i][1]-arr[i][0])
    arr[i].append(arr[i][2]/arr[i][3])
arr=sorted(arr,key=lambda x:(x[0],-x[4],x[1]))

capacity=0
delivery=[]
label=[[] for x in range(n-1)]
for maeul in range(n):
    for list in arr:
        if list[0]==maeul+1:
            label[maeul].append(list)

def check(i):
    if label[truck][i][2] <= delivery[0][2]:
        if label[truck][i][4] <= delivery[0][4]:
            return False
        else:
            delivery[0][2] -= label[truck][i][2]
            delivery[0][4] = delivery[0][2] / delivery[0][3]
            delivery.append(label[truck][i])
    else:
        if label[truck][i][4] <= delivery[0][4]:
            return False
        else:
            before_data = label[truck][i][2]
            label[truck][i][2] = delivery[0][2]
            label[truck][i][4] = label[truck][i][2] / label[truck][i][3]
            if label[truck][i][4] <= delivery[0][4]:
                return False
            del delivery[0]
            delivery.append(label[truck][i])
            label[truck][i][2] = before_data - label[truck][i][2]
            label[truck][i][4] = label[truck][i][2] / label[truck][i][3]
            check(i)

count=0

for truck in range(len(label)):

    for i in range(len(label[truck])):
        if capacity<c:
            capacity+=label[truck][i][2]
            if capacity>c:
                new_value=capacity-c
                label[truck][i][2]=label[truck][i][2]-new_value
                label[truck][i][4]=label[truck][i][2]/label[truck][i][3]
                capacity=c
            delivery.append(label[truck][i])
            delivery=sorted(delivery,key=lambda x:x[4])

        else:
            delivery = sorted(delivery, key=lambda x: x[4])
            check(i)

    for f in range(len(delivery)):
        delivery[f][3]=delivery[f][3]-1
        if delivery[f][3]!=0:
            delivery[f][4]=delivery[f][2]/delivery[f][3]

    delivery = sorted(delivery, key=lambda x: x[3])
    for k in range(len(delivery)):
        if delivery[0][3]==0:
            count+=delivery[0][2]
            capacity -= delivery[0][2]
            del delivery[0]

sum=0
sum+=count

print(sum)