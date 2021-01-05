"""
 상하좌우
 여행 계획서대로 이동 시 좌표값을 리턴
 - 입력
    첫 줄 - N : 정사각형 공간 크기
    둘째 줄 - : a가 이동하는 계획서
 - 리턴
    계획서대로 이동 시 도착 좌표 x y

 5
 R R R U D D
"""
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']
n = int(sys.stdin.readline().split()[0])
a_list = list(map(str, sys.stdin.readline().split()))
x, y = 1, 1

for a in a_list:
    for t in range(4):
        if a == types[t]:
            nx = x + dx[t]
            ny = y + dy[t]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x, y = nx, ny
print(x, y)


