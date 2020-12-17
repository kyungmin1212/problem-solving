t=int(input())

for _ in range(t):
    n,m=list(map(int,input().split()))
    data=[(int(x),idx) for idx,x in enumerate(input().split())]
    count=0
    while True:
        if data[0][0]==max(data,key=lambda x:x[0])[0]:
            count+=1
            if data[0][1]==m:
                print(count)
                break
            data.pop(0)
        else:
            data.append(data.pop(0))


