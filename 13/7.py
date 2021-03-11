"""
 인구 이동
"""
import sys
import copy
from collections import deque

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, sys.stdin.readline().split())  # n*n, 인구차이 l명 이상, r명 이하
arr = []
a_list = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def bfs(i, j, index):
    queue = deque()
    queue.append((i, j))
    # 합쳐진 국가를 담는 리스트
    united = list()
    united.append((i, j))

    visited[i][j] = index
    result = arr[i][j]  # 총 인구 수
    count = 1  # 국가 수
    while queue:
        x, y = queue.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] != -1:
                continue
            if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                queue.append((nx, ny))
                # 합치기
                visited[nx][ny] = index
                united.append((nx, ny))
                result += arr[nx][ny]
                count += 1
    # 인구 분배
    for x, y in united:
        arr[x][y] = result // count


answer = 0  # 총 인구 이동 수

while True:  # 인구 이동이 불가능할 때까지
    visited = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:  # 방문 처리가 안된 경우
                bfs(i, j, index)
                index += 1

    if index >= n * n:   # 인구이동을 더 이상 못하는 경우
        break
    answer += 1

print(answer)
