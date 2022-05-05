def solution(triangle):
    answer = 0
    for floor in range(1,len(triangle)):
        for index in range(len(triangle[floor])):
            if index==0:
                triangle[floor][index]+=triangle[floor-1][index]
            elif index==len(triangle[floor])-1:
                triangle[floor][index]+=triangle[floor-1][index-1]
            else:
                triangle[floor][index]+=max(triangle[floor-1][index-1],triangle[floor-1][index])
    return max(triangle[-1])