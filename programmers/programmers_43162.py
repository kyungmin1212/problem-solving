def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, computers):
    global parent
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1 and computers[j][i] == 1:
                union(i, j)

    answer_list = []
    for i in range(n):
        a = find(i)
        if a not in answer_list:
            answer_list.append(a)
    return len(answer_list)