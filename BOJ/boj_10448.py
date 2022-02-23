t=int(input())

eureka_num=set()

for i in range(1,46):
    a=(i*(i+1)/2)
    for j in range(1,46):
        b=(j*(j+1)/2)
        for k in range(1,46):
            c=(k*(k+1)/2)
            eureka_num.add(a+b+c)

for _ in range(t):
    v=int(input())
    if v in eureka_num:
        print(1)
    else:
        print(0)