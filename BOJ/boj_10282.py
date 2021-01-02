"""
문제 : 최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다!
이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다.
어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면
그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면,
a가 감염되더라도 b는 안전하다.
최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때,
해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며
그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 최대 100개이다.
각 테스트 케이스는 다음과 같이 이루어져 있다.
-첫째 줄에 컴퓨터 개수 n,의존성 개수 d, 해킹당한 컴퓨터의 번호 c가 주어진다
(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n).
-이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s가 주어진다
(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000).
이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후
컴퓨터 a도 감염됨을 뜻한다.
각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.
출력 : 각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수,
마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력한다.
"""
import heapq

def dijkstra(start):
    heap_data=[]
    heapq.heappush(heap_data,(0,start))
    # 처음 시작지점의 거리는 0 이므로 heap 에다가 (0,start)를 넣어준다.
    distance[start]=0
    while heap_data:
        # 거리가 짧은거부터 뽑아내기 위하여 heapq를 사용한것이다.
        dist,now=heapq.heappop(heap_data)
        # now 지점으로 이동했는데 한칸 이동하는 거리가 now지점까지 오는 다른 방법보다
        # 크다면 볼필요가 없다 .
        if distance[now]<dist:
            continue
        for i in adj[now]:
            # cost 는 시작지점부터 각각의 i[1] 시간만큼계속 더해지게 된다.
            cost =dist+i[1]
            # 다음지점의 거리가 cost보다 크다면 더짧은 값인 cost로 업데이트 시켜준다.
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                # 다음까지의 거리와 다음지점을 heapq에 넣어준다.
                heapq.heappush(heap_data,(cost,i[0]))

for _ in range(int(input())):
    n,m,start=map(int,input().split())
    adj=[[] for i in range(n+1)]
    distance=[1e9]*(n+1)
    for _ in range(m):
        x,y,cost=map(int,input().split())
        adj[y].append((x,cost))
    dijkstra(start)
    count=0
    max_distance=0
    for i in distance:
        if i !=1e9:
            count+=1
            if i>max_distance:
                max_distance=i
    print(count,max_distance)