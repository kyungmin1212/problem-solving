import copy

arr=[]

def plu(data,n):
    if len(data)==n:
        arr.append(copy.deepcopy(data))
        return
    data.append('a')
    plu(data,n)
    data.pop()

    data.append('b')
    plu(data,n)
    data.pop()

    data.append('c')
    plu(data,n)
    data.pop()

plu([],3)
print(arr)
arr=[]
plu([],4)
print(arr)