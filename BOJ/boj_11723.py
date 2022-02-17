import sys
input=sys.stdin.readline

m=int(input())

s=1<<20

for _ in range(m):
    input_list=input().split()
    if len(input_list)==2:
        order,number=input_list
        number=int(number)-1
    else:
        order=input_list[0]

    if order=='add':
        s=s|(1<<number)
    elif order=='remove':
        s=s&~(1<<number)
    elif order=='check':
        if s&(1<<number):
            print(1)
        else:
            print(0)
    elif order=='toggle':
        if s&(1<<number):
            s=s&~(1<<number)
        else:
            s=s|(1<<number)
    elif order=='all':
        s=(1<<20)-1
    elif order=='empty':
        s=s=1<<20