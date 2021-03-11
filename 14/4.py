"""
    카드 정렬하기
    https://www.acmicpc.net/problem/1715

3
10
20
40
"""

import heapq
import sys

n = int(sys.stdin.readline().split()[0])    # 카드 묶음
arr = []

for i in range(n):
    heapq.heappush(arr, int(sys.stdin.readline().split()[0]))

result = 0
while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    sum_val = first + second
    result += sum_val
    heapq.heappush(arr, sum_val)

print(result)





