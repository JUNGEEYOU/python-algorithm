"""
 1이 될 때까지
 n , k: 나누는 값
 - 규칙
    1. n에서 1 뺀다.
    2. n을 k로 나눈다.

"""
import sys

result = 0
n, k = map(int, sys.stdin.readline().split())

while True:
    target = (n // k) * k     # n이 k로 나눠지는 수
    result += (n - target)    # 1를 빼주는 횟수
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)
print(result)

