a=[1,1,3,4,3,2,5]
b=len(a)
for i in range(b):
    if a[i]<=3:
        del a[a.index(a[i])]
        print(a)
print(a)