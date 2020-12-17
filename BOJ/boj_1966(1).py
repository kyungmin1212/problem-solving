t=int(input())

for i in range(t):
    n,m=list(map(int,input().split()))
    data=list(map(int,input().split()))
    data2=[]
    for j in range(len(data)):
        data2.append([data[j],j])

    count=0
    while True:
        length = len(data2)
        max_value=data2[0][0]
        for l in range(1,length):
            if max_value<data2[l][0]:
                max_value=data2[l][0]

        while data2[0][0]!=max_value:
            data2.append(data2[0])
            del data2[0]
        count+=1

        if data2[0][1]==m:
            print(count)
            break
        del data2[0]