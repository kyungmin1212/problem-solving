"""
문제 : 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
입력 : 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
출력 : 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""
n,c=list(map(int,input().split()))
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start=1
end=arr[-1]-arr[0]
result=0
while start<=end:
    a=arr[0]
    count = 1
    mid=(start+end)//2
    a+=mid
    for i in range(1,len(arr)):
        if arr[i]>=a:
            a=arr[i]+mid
            count+=1
    if count>=c:  # c개 이상의 공유기를 설치할수 있는경우( 이상으로 설정할때는 값은 나왔지만 거리를 더키워보고싶은경우)
        result=mid
        start=mid+1
    else:       # c개 미만의 공유기를 설치하는경우
        end=mid-1
print(result)
    # if count<=c: # c개 이하의 공유기를 설치하는 경우 ( 이하로 설정할때는 값은 나왔지만 거리를 더 좁혀보고싶은경우)
    #     result=mid
    #     end=mid-1
    # else:        # c개 초과의 공유기를 설치하는경우
    #     start=mid+1
# 두개의 차이를 명확하게 알아야한다. count>=설정가능 공유기수 이렇게 설정하면
# mid 값을 최대한 키울때 까지 실행한다. mid 의 최댓값을 구하게 된다.
# count<=설정 가능 공유 기수 이렇게 설명하면
# count가 똑같을때 mid 값을 최대한 작게 만들어준다 .
