a=[1,2,3,4]

for i in a:
    print(i)
    if i==2:
        print("hi")
        a.remove(2)


print(a)