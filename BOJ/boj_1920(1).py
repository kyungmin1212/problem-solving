n=int(input())
arr=[int(x) for x in input().split()]
m=int(input())
arr2=[int(x) for x in input().split()]
arr.sort()

for i in arr2:
    start=0
    end=len(arr)-1

    while start<=end:
        mid = int((start + end) / 2)
        if arr[mid]<i:
            result=arr[mid]
            start=mid+1
        elif arr[mid]>i:
            end=mid-1
        elif arr[mid]==i:
            print(1)
            break

    if start>end:

        print(0)