"""
 큰 수의 법칙
 N개의 자연수 리스트, M 개의 수를 선택, K 만큼 연속 가능.
 가장 큰 수를 리턴한다.

 예시 입력
 5 8 3
 2 4 5 4 6
"""
import sys
N, M, K = list(map(int, sys.stdin.readline().split()))
number = list(map(int, sys.stdin.readline().split()))
number.sort(reverse=True)
first = number[0]
second = number[1]
answer = 0
count = 0
for _ in range(M):
    if count == K:
        count = 0
        answer += second
    else:
        answer += first
        count += 1

print(answer)



