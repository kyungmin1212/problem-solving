k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))
arr.sort()

min=1
max=arr[-1]
result=0
while min<=max:
    mid=(min+max)//2
    count=0
    for i in range(len(arr)):
        count+=arr[i]//mid
    if count>=n: #더많이 잘라진경우 크기를 키워서 잘라야함
        min=mid+1
        result=mid
    else: # 더작게잘린경우 크기를 줄여서 잘라야함
        max=mid-1

print(result)