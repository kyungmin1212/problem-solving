import copy

def recursive(array, n):
    if len(array) == n:
        buho.append(copy.deepcopy(array))
        return

    array.append(" ")
    recursive(array, n)
    array.pop()

    array.append("+")
    recursive(array, n)
    array.pop()

    array.append("-")
    recursive(array, n)
    array.pop()

t=int(input())
for _ in range(t):
    n=int(input())
    arr=[x for x in range(1,n+1)]
    buho=[]
    recursive([],n-1)

    for i in range(len(buho)):
        string =""
        for j in range(len(buho[i])):
            string+=str(arr[j])+buho[i][j]
        string+=str(arr[-1])
        if eval(string.replace(" ",""))==0:
            print(string)
    print("")

