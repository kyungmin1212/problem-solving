A=list(input())
B=list(input())
A.insert(0,"plus")
B.insert(0,"plus")

lcs=[["" for _ in range(len(A))] for _ in range(len(B))]

for i in range(1,len(B)):
    for j in range(1,len(A)):
        if B[i]==A[j]:
            lcs[i][j]=lcs[i-1][j-1]+B[i]
        else:
            if len(lcs[i-1][j])>=len(lcs[i][j-1]):
                lcs[i][j]=lcs[i-1][j]
            else:
                lcs[i][j]=lcs[i][j-1]

print(len(lcs[-1][-1]))
print(lcs[-1][-1])
