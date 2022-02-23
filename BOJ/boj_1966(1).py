from collections import deque
from heapq import heappush,heappop

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    q=deque()
    hq=[]
    prior_list=list(map(int,input().split()))
    for i in range(n):
        q.append((prior_list[i],i))
        heappush(hq,(-prior_list[i]))

    count=0
    while hq:
        flag=False
        count+=1
        check_prior=-heappop(hq)
        while True:
            prior, index = q.popleft()
            if check_prior==prior and index==m:
                flag=True
                print(count)
                break
            elif check_prior==prior:
                break
            else:
                q.append((prior,index))
        if flag:
            break
