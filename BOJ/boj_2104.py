n=int(input())

array_list=list(map(int,input().split()))

answer=0

def check(start,end):
    global answer
    if start==end:
        answer=max(answer,array_list[start]**2)
    elif start==end-1:
        answer=max(answer,array_list[start]**2,array_list[end]**2)
    else:
        mid=(start+end)//2
        # left
        check(start,mid)
        # right
        check(mid+1,end)
        # mid
        start_point=mid-1
        end_point=mid+1
        sum_value=array_list[mid]
        min_value=array_list[mid]
        while start_point>=start or end_point<=end:
            if start_point==start-1:
                sum_value+=array_list[end_point]
                min_value=min(min_value,array_list[end_point])
                answer=max(answer,sum_value*min_value)
                end_point+=1

            elif end_point==end+1:
                sum_value+=array_list[start_point]
                min_value=min(min_value,array_list[start_point])
                answer=max(answer,sum_value*min_value)
                start_point-=1

            elif array_list[start_point]<=array_list[end_point]:
                sum_value+=array_list[end_point]
                min_value=min(min_value,array_list[end_point])
                answer=max(answer,sum_value*min_value)
                end_point += 1

            elif array_list[start_point] > array_list[end_point]:
                sum_value+=array_list[start_point]
                min_value=min(min_value,array_list[start_point])
                answer=max(answer,sum_value*min_value)
                start_point-=1

check(0,len(array_list)-1)
print(answer)