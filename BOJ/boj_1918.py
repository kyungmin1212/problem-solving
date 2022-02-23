from collections import deque

priority={"+":0,"-":0,"*":1,"/":1,"(":2}

string=input()

ans=""
stack=deque()

for s in string:
    if s.isalpha():
        ans+=s
    else:
        if len(stack)==0:
            stack.append(s)
        elif s==")":
            while stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        else:
            if priority[s]>priority[stack[-1]] or stack[-1]=="(":
                stack.append(s)
            else:
                while True:
                    if len(stack)==0:
                        break
                    if stack[-1]=="(":
                        break
                    if priority[stack[-1]]>=priority[s]:
                        ans+=stack.pop()
                    else:
                        break
                stack.append(s)


while stack:
    ans+=stack.pop()
print(ans)