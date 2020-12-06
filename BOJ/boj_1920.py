"""
문제 : N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
입력 : 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
출력 : M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""
import sys
n=int(sys.stdin.readline())
n_list=[int(x) for x in sys.stdin.readline().split()]
m=int(sys.stdin.readline())
m_list=[int(x) for x in sys.stdin.readline().split()]
n_list=sorted(n_list)

for i in m_list:
    start, end = 0, n - 1
    while start<=end:
        a=(start+end)//2
        mid=n_list[a]
        if i>mid:
            start=a+1
        elif i<mid:
            end=a-1
        elif i==mid:
            print(1)
            break
    if start>end:
        print(0)