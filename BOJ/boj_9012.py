from collections import deque
n=int(input())

for _ in range(n):
    string_list=list(input())
    stack=deque()
    flag=False
    for item in string_list:
        if item=="(":
            stack.append(1)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                print("NO")
                flag=True
                break
    if flag:
        continue
    if len(stack)>0:
        print("NO")
    else:
        print("YES")