"""
문제 : 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자
(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다).
이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.
N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.
입력 : 첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).
각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).
출력 : 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다.
각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
"""
t=int(input())

data=[]
for i in range(0,9):
    data.append([])

data[0]=[[1,[]]]
data[1]=[[3,["+"]],[-1,["-"]],[12,[" "]]]

for i in range(2,9):
    for j in range(len(data[i-1])):
        data[i].append([data[i-1][j][0]+(i+1),data[i-1][j][1]+["+"]])
        data[i].append([data[i-1][j][0]-(i+1),data[i-1][j][1]+["-"]])
    for j in range(len(data[i-2])):
        data[i].append([data[i-2][j][0]+((i)*10+(i+1)),data[i-2][j][1]+["+"," "]])
        data[i].append([data[i-2][j][0]-((i)*10+(i+1)),data[i-2][j][1]+["-"," "]])

for k in range(t):
    n=int(input())
    result = []
    for i in range(len(data[n-1])):
        if data[n-1][i][0]==0:
            a=[]
            for j in range(1,n):
                a.append(str(j))
                a.append(data[n-1][i][1][j-1])
            a.append(str(n))
            result.append(a)
    result.sort()
    for m in result:
        print("".join(m))
    print("")
