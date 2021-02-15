"""
 벽 또는 자신의 몸과 부딪히면 끝
 x초 끝나고 l: 왼쪽 , d가 오른쪽으로 90도 방향 회전
"""

import sys
from collections import deque

n = int(sys.stdin.readline().split()[0])   # 보드의 크기
k = int(sys.stdin.readline().split()[0])   # 사과 개수

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = -1      # 사과를 의미

l = int(sys.stdin.readline().split()[0])   # 뱀의 변환 횟수
loc = deque()
for _ in range(l):
    x, y = map(str, sys.stdin.readline().split())
    loc.append((int(x), y))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0   # 몇 초에 끝나는지

nx, ny = 1 , 1   # 머리 위치
graph[1][1] = 1
body = deque()
body.append((1, 1))
dir = 0    # 방향 - 동

while True:
    nx = nx + dx[dir]
    ny = ny + dy[dir]
    if nx < 1 or nx > n or ny < 1 or ny > n:  # 범위에 벗어나는 경우
        break
    if graph[nx][ny] == 1:   # 몸통에 부딪힌 경우
        break

    if graph[nx][ny] == -1:  # 사과 존재
        graph[nx][ny] = 1
    else:                              # 사과 없음 > 꼬리 빈칸
        graph[nx][ny] = 1
        body_x, body_y = body.popleft()
        graph[body_x][body_y] = 0

    body.append((nx, ny))

    time += 1
    if loc and loc[0][0] == time:   # 위치 바꾸기
        a, b = loc.popleft()   # 초, 방향
        if b == 'L':       # 왼쪽 90 회전
            dir = (dir - 1) % 4
        else:              # 오른쪽 90 회전
            dir = (dir + 1) % 4


print(time + 1)