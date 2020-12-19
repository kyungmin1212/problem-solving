# merge sort 한번에 코드로 짜는 방법

def merge_split(data):
    if len(data)<=1:
        return data
    mid=int(len(data)/2)
    left=merge_split(data[:mid])
    right=merge_split(data[mid:])
    return merge(left,right)

def merge(left,right):
    left_index=0
    right_index=0
    arr=[]
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            arr.append(left[left_index])
            left_index+=1
        else:
            arr.append(right[right_index])
            right_index+=1

    while left_index<len(left):
        arr.append(left[left_index])
        left_index += 1

    while right_index<len(right):
        arr.append(right[right_index])
        right_index += 1

    return arr

n=int(input())
array=[]

for _ in range(n):
    array.append(int(input()))

array=merge_split(array)

for data in array:
    print(data)