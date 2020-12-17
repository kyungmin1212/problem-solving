N,M=map(int,input().split())
arr=list(map(int,input().split()))
hap=set()

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            continue
        for k in range(len(arr)):
            if arr[i]==arr[k] or arr[j]==arr[k]:
                continue
            hap.add(arr[i]+arr[j]+arr[k])

hap=sorted(hap)
start=0
end=len(hap)-1
while start<=end:
    mid = (start + end) // 2
    if hap[mid]<=M:
        result=hap[mid]
        start=mid+1
    elif hap[mid]>M:
        end=mid-1

print(result)