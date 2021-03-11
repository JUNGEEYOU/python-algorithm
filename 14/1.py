"""
    국영수
    https://www.acmicpc.net/problem/10825
    국어: 내림차순
    영어: 오름차순
    수학: 내림차순
    이름: 사전순
"""
import sys

n = int(sys.stdin.readline().split()[0])    # 학생의 수

result = []
for _ in range(n):
    a, b, c, d = map(str, sys.stdin.readline().split())
    result.append((int(b), int(c), int(d), a))

result.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for i in range(n):
    print(result[i][3])



