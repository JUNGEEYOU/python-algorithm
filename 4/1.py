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

n = int(sys.stdin.readline().split()[0])
array = list(map(str, sys.stdin.readline().split()))
result = (1, 1)
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for a in array:
    x = result[0] + move[a][0]
    y = result[1] + move[a][1]

    if x < 1 or y < 1 or x > n or y > n:
        continue
    result = (x, y)

print(result[0], result[1])