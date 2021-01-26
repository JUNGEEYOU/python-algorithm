"""
 왕실의 나이트
 8 * 8 좌표에 나이트는 두가지 경우의 수로만 이동이 가능하다.
 1. 오른쪽으로 두 칸 이동 후 아래로 한 칸 이동
 2. 아래로 두 칸 이동 후 오른쪽으로 한 칸 이동
 - 입력
    현재 나이트가 위치한 곳의 좌표
 - 리턴
    나이트가 이동할 수 있는 경우의 수
* 참고
ord('a')   - 아스키 값으로 변경
97

"""

import sys
location = str(sys.stdin.readline().split()[0])
x = int(ord(location[0]) - ord('a')) + 1
y = int(location[1])
result = 0
# 가능한 경우의 좌표
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        result += 1
print(result)

