"""
 개미 전사
 1. 테이블 정의: 해당 위치에서 최댓값
 2. 점화식 찾기: max(i - 1 최대값, 현 위치 + (i - 2 최대값))
 3. 초기값 설정: 0, 1 초기화

4
1 3 1 5
"""
import sys

n = int(sys.stdin.readline().split()[0])
array = list(map(int, sys.stdin.readline().split()))

d = [0] * n
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])