"""
 볼링공 고르기
 서로 다른 무개의 공 고르기
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

방법 1 완탐
방법 2 그리디: 경우의 수 세기.
"""
import sys

n, m = map(int, sys.stdin.readline().split())   # n 개의 공, m 최대 공 무게
k = list(map(int, sys.stdin.readline().split()))  # 공 무게

array = [0] * 11

for i in k:
    array[i] += 1


result = 0

for i in range(1, m + 1):     # 공을 하나씩 꺼내서 경우 수 세기
    n -= array[i]             # 전체 공의 수 - 현재 공의 수
    result += array[i] * n    # a는 arr[i] 선택한 경우 * 나머지 공의 조합

print(result)