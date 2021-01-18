"""
    국영수
    https://www.acmicpc.net/problem/10825
    국어: 내림차순
    영어: 오름차순
    수학: 내림차순
    이름: 사전순
"""

import sys


n = int(sys.stdin.readline().split()[0])
array = []
for _ in range(n):
    a, b, c, d = list(map(str, sys.stdin.readline().split()))
    array.append((a, int(b), int(c), int(d)))
array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in array:
    print(a[0])

