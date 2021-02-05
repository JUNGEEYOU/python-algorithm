"""
 볼링공 고르기
 서로 다른 무개의 공 고르기
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

방법 1 완탐
"""
import sys

n, m = map(int, sys.stdin.readline().split())   # n 개의 공, m 최대 공 무게
k = list(map(int, sys.stdin.readline().split()))  # 공 무게

result = 0
for i in range(n - 1):
    for j in range(i, n):
        if k[i] != k[j]:
            result += 1

print(result)