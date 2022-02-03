n,m=map(int,input().split())

heights=list(map(int,input().split()))

start=0
end=int(1e9)

while start<=end:
    mid=(start+end)//2
    count=0
    for item in heights:
        minus=item-mid
        if minus>0:
            count+=minus
    if count>=m:
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)