"""
 미로 탈출
     5 6
    101010
    111111
    000001
    111111
    111111
"""

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())   # 세로 가로
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    result += 1
    for a in range(4):
        nx = dx[a] + x
        ny = dy[a] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:    # 처음 방문하는 경우
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])