"""
 1이 될 때까지
 n , k: 나누는 값
 - 규칙
    1. n에서 1 뺀다.
    2. n을 k로 나눈다.

"""
import sys


n, k = map(int, sys.stdin.readline().split())
result = 0

while 1:
    if n == 1:
        break
    if n % k == 0:
        n = n // k
    else:
        n = n - 1
    result += 1
print(result)