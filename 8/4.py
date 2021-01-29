"""
    1로 만들기
    https://www.acmicpc.net/problem/1463 비슷한 문제
"""
import sys


n = int(sys.stdin.readline().split()[0])
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)


print(d[n])

