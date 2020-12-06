"""
문제 : 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
입력 : 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
출력 : 주어진 수들 중 소수의 개수를 출력한다.
"""
import sys
import math
n=int(sys.stdin.readline())
n_list=[int(x) for x in sys.stdin.readline().split()]
def is_prime_number(data):
    if data==1:
        return False
    for j in range(2,int(math.sqrt(data))+1):
        if data%j==0:
            return False
    return True
prime_number=[]
for i in n_list:
    if is_prime_number(i):
        prime_number.append(i)
print(len(prime_number))
