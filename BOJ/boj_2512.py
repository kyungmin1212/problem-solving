n=int(input())
asset=list(map(int,input().split()))
total=int(input())
max_value=max(asset)
start=1
end=max(asset)
while start<=end:
    mid=(start+end)//2
    count=0
    for i in range(n):
        if asset[i]<=mid:
            count+=asset[i]
        else:
            count+=mid
    if count>total:
        end=mid-1
    elif count<=total:
        start=mid+1
        result=mid
print(result)
