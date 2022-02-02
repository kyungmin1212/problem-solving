a,b,c=map(int,input().split())

def count(b):
    if b==1:
        return a%c
    elif b%2==1:
        return count(b//2)**2*a%c
    else:
        return count(b//2)**2%c

print(count(b))