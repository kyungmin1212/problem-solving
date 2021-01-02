"""
문제 : 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다.
김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다.
둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
출력 : 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다.
만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
"""
from collections import Counter

n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())

arr_counter=Counter(arr)
arr_sort=arr_counter.most_common()
arr_sort.sort(key=lambda x:(-x[1],x[0]))
print(arr_sort[0][0])
# # arr_counter : Counter을 통해 만들어진 객체는 딕셔너리 형태로 저장되어있다.
# # 먼저 arr_counter.most_common(1) 을 통하여 첫번째로 제일 많은 것을 프린트한다 [('blue',3)]
# print(arr_counter.most_common(1))
# # 이런식으로 리스트안에 튜플형태로 저장되어 있다.
# # 횟수를 출력하고 싶으면은
# print(arr_counter.most_common(1)[0][1])
# # 이름을 출력하고 싶으면은
# print(arr_counter.most_common(1)[0][0])
# # arr_counter.most_common(2) 를 사용하면 두번째로 제일 많은것 까지 프린트를 해준다. [('blue',3),('red',2)]
# print(arr_counter.most_common(2))
# # 괄호안에 수를 안넣으면 정렬된 순으로 쭉 나열되게 된다.
# print(arr_counter.most_common())