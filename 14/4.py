"""
    카드 정렬하기
    https://www.acmicpc.net/problem/1715

3
10
20
40
"""
import sys
import heapq

n = int(sys.stdin.readline().split()[0])
array = list()
result = 0

for _ in range(n):
    heapq.heappush(array, int(sys.stdin.readline().split()[0]))

while len(array) > 1:
    first = heapq.heappop(array)
    second = heapq.heappop(array)
    sum_val = first + second
    result += sum_val
    heapq.heappush(array, sum_val)

print(result)





