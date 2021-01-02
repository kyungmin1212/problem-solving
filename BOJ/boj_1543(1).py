string=input()
word=input()

index=0
result=0

while len(string)>index:
    if string[index:index+len(word)]==word:
        result+=1
        index+=len(word)
    else:
        index+=1

print(result)