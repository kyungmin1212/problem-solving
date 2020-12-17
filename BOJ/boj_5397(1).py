t=int(input())

for _ in range(t):
    data=list(input())
    result=[]
    save=[]
    for i in data:
        if i=="<":
            if result:
                save.append(result.pop())
        elif i==">":
            if save:
                result.append(save.pop())
        elif i=="-":
            if result:
                result.pop()
        else:
            result.append(i)


    result.extend(reversed(save))
    print("".join(result))