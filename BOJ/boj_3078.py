from collections import defaultdict
from collections import deque

n,k=map(int,input().split())
count=defaultdict(int)
q=deque()
check_word=input()
check_len=len(check_word)
answer=0

for _ in range(1,n):
    if len(q)<k:
        word=input()
        len_word=len(word)
        q.append(word)
        count[len_word]+=1
    else:
        answer+=count[check_len]
        check_word=q.popleft()
        check_len=len(check_word)
        count[check_len]-=1

        word=input()
        len_word=len(word)
        q.append(word)
        count[len_word]+=1

while q:
    answer += count[check_len]
    check_word = q.popleft()
    check_len = len(check_word)
    count[check_len] -= 1

print(answer)
