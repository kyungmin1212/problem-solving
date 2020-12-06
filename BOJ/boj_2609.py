"""
문제 : 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
출력 : 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""
import sys
m,n=map(int,sys.stdin.readline().split())
data=[]
m_mem=[]
n_mem=[]
def divide(m,n):
    for i in range(2,min(m,n)+1):
        if m%i==0 and n%i==0:
            m=int(m/i)
            n=int(n/i)
            data.append(i)
            divide(m,n)
            break
    m_mem.append(m)
    n_mem.append(n)
    return m,n
divide(m,n)
a=1
for i in data:
    a*=i
max_number=a
min_number=a*m_mem[0]*n_mem[0]
print(max_number)
print(min_number)