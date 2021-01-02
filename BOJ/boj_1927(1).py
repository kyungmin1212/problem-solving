import heapq

heap=[]
result=[]

n=int(input())

for _ in range(n):
    a=int(input())
    if a==0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap,a)

for data in result:
    print(data)