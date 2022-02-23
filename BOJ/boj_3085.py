from copy import deepcopy

n=int(input())

candy=[list(input()) for _ in range(n)]

# row는 0부터 n-1까지 ,column 은 0부터 n-2까지만
def change_value(candy,row,column):
    new_candy=deepcopy(candy)
    new_candy[row][column+1],new_candy[row][column]=new_candy[row][column],new_candy[row][column+1]
    return new_candy

def check_max(candy_map):
    max_count=0
    count = 0
    before_data = 0
    for row in range(n):
        for column in range(n):
            if candy_map[row][column]!=before_data:
                before_data=candy_map[row][column]
                if count>max_count:
                    max_count=count
                count=1
            else:
                count+=1
        if count>max_count:
            max_count=count
        count = 0
        before_data = 0
    return max_count

answer=0
for i in range(n):
    for j in range(n-1):
        new_candy_map_1=change_value(candy,i,j)
        new_candy_map_2=change_value(list(map(list,zip(*candy))),i,j)
        answer=max(answer,check_max(new_candy_map_1),check_max(list(zip(*new_candy_map_1))),check_max(new_candy_map_2),check_max(list(zip(*new_candy_map_2))))
print(answer)


