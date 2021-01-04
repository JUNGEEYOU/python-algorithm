"""
 큰 수의 법칙 - 방법 2. 횟수로 계산하기
 N개의 자연수 리스트, M 개의 수를 선택, K 만큼 연속 가능.
 가장 큰 수를 리턴한다.

 예시 입력
 5 8 3
 2 4 5 4 6
"""
import sys

N, M, K = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort(reverse=True)
first = number[0]
second = number[1]
answer = 0

# 가장 큰 수가 더해지는 횟수 계산
count = M // (K + 1) * K      # 나눠 떨어지는 경우. 가장 큰수가 등장하는 횟수
count += M % (K + 1)          # 나눠 떨어지지 않는 경우. 나머지는 모두 큰수 횟수로 추가

answer += (count * first)
answer += (M - count) * second

print(answer)
