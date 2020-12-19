"""
문제 : 민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다.
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때,
두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.
입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다.
각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다.
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.
친구 관계는 두 사용자의 아이디로 이루어져 있으며,
알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.
출력 : 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""
# 결과는 잘나오지만 시간초과 나는 함수 일일히 다 비교하기 때문이다.
# 올바른 정답은 boj_4195(1) 참고

import sys
t=int(sys.stdin.readline())

for _ in range(t):
    friend_list=[[]]
    f = int(sys.stdin.readline())
    for i in range(f):
        a,b=sys.stdin.readline().split()
        count=0
        check=0
        if not friend_list[0]:
            count+=2
            friend_list[0].append(a)
            friend_list[0].append(b)
            check=2
        else:
            for j in range(len(friend_list)):
                if check==2:
                    break
                elif a not in friend_list[j] and b not in friend_list[j]:
                    continue
                elif a in friend_list[j] and b in friend_list[j]:
                    check=2
                    count+=len(friend_list[j])
                elif a in friend_list[j] and check==0:
                    check+=1
                    count+=len(friend_list[j])
                    c=j
                    acheck=True
                elif b in friend_list[j] and check==0:
                    check+=1
                    count+=len(friend_list[j])
                    c=j
                    bcheck=True
                elif a in friend_list[j] and check==1:
                    check=2
                    count+=len(friend_list[j])
                    friend_list[c]=friend_list[c]+friend_list[j]
                    del friend_list[j]
                elif b in friend_list[j] and check==1:
                    check=2
                    count+=len(friend_list[j])
                    friend_list[c]=friend_list[c]+friend_list[j]
                    del friend_list[j]
                    bcheck=True

            if check<2:
                if check==1 and acheck:
                    count=2
                    friend_list[c].append(b)
                elif check==1 and bcheck:
                    count=2
                    friend_list[c].append(a)
                elif check==0:
                    friend_list.append([a,b])
                    count=2
        print(count)



