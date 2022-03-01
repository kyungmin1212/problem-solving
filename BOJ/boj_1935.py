from collections import deque

n=int(input())

expression=input()
number=[]
for _ in range(n):
    number.append(int(input()))

check_dict=dict()
for index,s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if index>=len(number):
        break
    check_dict[s]=number[index]

cal_num=deque()
buho=deque()

for s in expression:
    if s.isalpha() and len(buho)==0:
        cal_num.append(check_dict[s])
    elif s.isalpha() and len(buho)!=0:
        while buho:
            num_1=cal_num.pop()
            num_2=cal_num.pop()
            bu=buho.popleft()
            cal_num.append(eval(f"{str(num_2)}{bu}{str(num_1)}"))
        cal_num.append(check_dict[s])
    else:
        buho.append(s)

while buho:
    num_1=cal_num.pop()
    num_2=cal_num.pop()
    bu=buho.popleft()
    cal_num.append(eval(f"{str(num_2)}{bu}{str(num_1)}"))

print(f'{cal_num[-1]:.2f}')