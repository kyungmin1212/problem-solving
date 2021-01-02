"""
문제 : 널리 잘 알려진 자료구조 중 최소 힙이 있다.
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
입력 : 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
입력되는 자연수는 231보다 작다.
출력 : 입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
"""

# 직접 일일히 내가 다 구현한 코드
n=int(input())

arr=[None]
answer=[]
def insert(node):
    arr.append(node)
    idx=len(arr)-1
    if idx>=2:
        insert_check(idx)

def insert_check(idx):
    if arr[idx]<arr[idx//2]:
        arr[idx],arr[idx//2]=arr[idx//2],arr[idx]
        if idx//2>=2:
            insert_check(idx//2)
    else:
        return

def heap_pop():
    if len(arr)==1:
        answer.append(0)
    else:
        result=arr[1]
        arr[1]=arr[-1]
        del arr[-1]
        if len(arr)>=3:
            pop_check(1)
        answer.append(result)

def pop_check(idx):
    if len(arr)>=4:
        if arr[idx]<=arr[idx*2]and arr[idx]<=arr[idx*2+1]:
            return
        elif arr[idx]<=arr[idx*2] and arr[idx]>arr[idx*2+1]:
            arr[idx],arr[idx*2+1]=arr[idx*2+1],arr[idx]
        elif arr[idx]>arr[idx*2] and arr[idx]<=arr[idx*2+1]:
            arr[idx],arr[idx*2]=arr[idx*2],arr[idx]
        else:
            if arr[idx*2]<arr[idx*2+1]:
                arr[idx],arr[idx*2]=arr[idx*2],arr[idx]
            else:
                arr[idx], arr[idx * 2 + 1] = arr[idx * 2 + 1], arr[idx]
    elif len(arr)==3:
        if arr[idx]<=arr[idx*2]:
            return
        else:
            arr[idx],arr[idx*2]=arr[idx*2],arr[idx]
    else:
        return



for _ in range(n):
    a=int(input())
    if a==0:
        heap_pop()
    else:
        insert(a)

for data in answer:
    print(data)