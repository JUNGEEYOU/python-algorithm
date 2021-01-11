"""
 음료수 얼려 먹기
    4 5
    00110
    00011
    11111
    00000
"""
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())   # 세로 가로
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for a in range(4):
                    nx = dx[a] + x
                    ny = dy[a] + y
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if graph[nx][ny] != 0:
                        continue
                    queue.append((nx, ny))
                    graph[nx][ny] = 1
print(result)