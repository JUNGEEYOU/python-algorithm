"""
 연구소. https://www.acmicpc.net/problem/14502
"""
import sys
import itertools
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(graph, stack, n, m):
    """
    바이러스 퍼트리기
    :return:
    """
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] != 0:
                continue
            stack.append((nx, ny))
            graph[nx][ny] = 2
    return graph

def get_zero_num(graph, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


n, m = map(int, sys.stdin.readline().split())  # 세로 가로
graph = []
array = []  # 0인 좌표 담기
array_two = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    zero = [(i, j) for j in range(len(a)) if a[j] == 0]
    two = [(i, j) for j in range(len(a)) if a[j] == 2]
    if zero: array.extend(zero)
    if two: array_two.extend(two)
    graph.append(a)

cn3 = itertools.combinations(array, 3)  # 3개의 벽 조합
result = 0  # 안전 영역 최대 크기

graph_temp = copy.deepcopy(graph)
array_two_temp = copy.deepcopy(array_two)
for c in cn3:
    # 벽 만들기
    for i in c:
        graph[i[0]][i[1]] = 1
    # 바이러스 퍼지게 하기
    graph = dfs(graph, array_two, n, m)
    # 0인 수 저장
    zero_num = get_zero_num(graph, n, m)
    result = max(result, zero_num)
    # 그래프 초기화
    graph = copy.deepcopy(graph_temp)
    array_two = copy.deepcopy(array_two_temp)

print(result)