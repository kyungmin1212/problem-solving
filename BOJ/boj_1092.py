"""
문제 : 지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다.
모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
모든 크레인은 동시에 움직인다.
각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다.
셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다.
넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.
출력 : 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다.
만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.
"""
# 내가 푼방식

n=int(input())
crain=[x for x in list(map(int,input().split()))]
m=int(input())
box=[x for x in list(map(int,input().split()))]
crain.sort()
box.sort()
def resultcheck(i):
    if resultcount[i] - 1 == 0:
        resultcount[i] = 0
    elif resultcount[i] - 1 > 0:
        resultcount[i] -= 1
    elif resultcount[i] - 1 < 0 and i<n-1:
        resultcheck(i+1)

if box[-1]>crain[-1]:
    print(-1)
else:
    resultlist=[[] for _ in range(len(crain))]
    boxcheck=[False]*len(box)
    for i in range(len(crain)):
        for j in range(len(box)):
            if box[j]<=crain[i] and not(boxcheck[j]):
                resultlist[i].append(box[j])
                boxcheck[j]=True
    resultcount=[]

    for i in resultlist:
        resultcount.append(len(i))
    resultcount=resultcount[::-1]
    count=0
    check=False
    while not(check):
        check=True
        for i in resultcount:
            if i!=0:
                check=False
        if check==True:
            break
        count+=1
        for i in range(len(resultcount)):
            resultcheck(i)

    print(count)