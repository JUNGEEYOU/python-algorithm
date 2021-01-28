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

result = 0 # 최종 절단기 길이
while left <= right:
    mid = (left + right) // 2  # 절단기의 길이
    total = 0        # 손님이 얻을 수 있는 떡 길이
    for a in array:
        if a > mid:
            total += a - mid
    if total >= m:   # 절단기 길이 늘리기 & 적어도 m 만큼이니 m보다 큰 떡길이는 정답이 될 수도 있으니 결과에 넣기
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)





