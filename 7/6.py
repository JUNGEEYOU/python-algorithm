"""
    떡볶이 떡 만들기 - 파라메트릭 서치
    4 6
    19 15 10 17
"""
import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(array)

while left <= right:
    mid = (left + right) // 2
    total = 0
    for a in array:
        if a > mid:
            total += a - mid
    if total >= m:   # 떡 양이 충분하지만 절단기 최댓값을 얻기 위함
        result = mid
        left = mid + 1
    else:             # 떡 양이 적어 절단기를 줄인다.
        right = mid - 1

print(result)