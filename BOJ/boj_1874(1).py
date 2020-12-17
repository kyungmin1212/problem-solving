n=int(input())
count=1
stack=[]
result=[]

for i in range(n):
    number=int(input())
    while count<=number:
        stack.append(count)
        result.append("+")
        count+=1
    if stack[-1]==number:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(result))