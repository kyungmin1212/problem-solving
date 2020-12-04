import sys
n=int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
push_count=0
pop_count=0
count=[]
i=0
while i<n:
    if i==0:
        push_count+=arr[0]
        count.append(["+",push_count])
        count.append(["-",1])
        pop_count+=1
    elif arr[i-1]<arr[i]:
        a=arr[:i]
        m=max(a)
        push_count+=arr[i]-m
        count.append(["+",arr[i]-m])
        count.append(["-",1])
        pop_count+=1
    elif arr[i-1]>arr[i]:
        pop_count+=1
        count.append(["-",1])
    i+=1
if push_count==n and pop_count==n:
    for i in count:
        print(f"{i[0]}\n"*i[1],end="")
else:
    print("NO")
