"""
 게임 개발

 - 입력

 - 리턴

"""
import sys

n, m = map(int, sys.stdin.readline().split())    # 세로, 가로
x, y, direction = map(int, sys.stdin.readline().split()) # (x, y) d(바라보는 방향)

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction= 3

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

