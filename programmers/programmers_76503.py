import sys

sys.setrecursionlimit(300000)


def dfs(node):
    global count
    visitied[node] = True

    for next_node in graph[node]:
        if not visitied[next_node]:
            value = dfs(next_node)
            node_value[node] += value
            count += abs(value)

    return node_value[node]


def solution(a, edges):
    global node_value, visitied, count, graph
    node_value = a[:]
    count = 0

    if sum(a) != 0:
        return -1

    visitied = [False for _ in range(len(a))]

    graph = [[] for _ in range(len(a))]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    dfs(0)
    return count