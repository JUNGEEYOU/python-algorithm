"""
 경쟁적 전염
 https://www.acmicpc.net/problem/18405
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())  # n*n, 1~k 바이러스 크기
graph = []
queue = deque()
filter_array = list()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    filter_array.extend([(i, y, v) for y, v in enumerate(array) if v > 0])
    graph.append(array)

s, x, y = map(int, sys.stdin.readline().split())   # 시간, (x, y)

filter_array.sort(key=lambda a: a[2])
for array in filter_array:
    queue.append((array[0], array[1], array[2]))


# bfs
while s and queue:
    if graph[x-1][y-1] != 0:
        break
    s -= 1
    len_arr = len(queue)
    for j in range(len_arr):
        (x1, y1, z) = queue.popleft()
        for i in range(4):
            xn = x1 + dx[i]
            yn = y1 + dy[i]

            if xn < 0 or yn < 0 or xn >= n or yn >= n:
                continue
            if graph[xn][yn] != 0:
                continue

            queue.append((xn, yn, z))
            graph[xn][yn] = z

print(graph[x-1][y-1])


