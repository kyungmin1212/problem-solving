from collections import defaultdict
import heapq
n,m=map(int,input().split())

primary_dict=defaultdict(list)
degree=defaultdict(int)
result=[]
heap=[]

for _ in range(m):
    x,y=map(int,input().split())
    primary_dict[x].append(y)
    degree[y]+=1

for i in range(1,n+1):
    if i not in degree:
        heapq.heappush(heap,i)

while heap:
    data=heapq.heappop(heap)
    result.append(data)
    if data in primary_dict:
        for i in primary_dict[data]:
            degree[i]-=1
            if degree[i]==0:
                heapq.heappush(heap,i)

for i in result:
    print(i,end=" ")