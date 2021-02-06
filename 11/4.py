"""
    만들 수 없는 금액
    - 입력
        첫 줄 - n : 동전의 개수
        둘째 줄 : 화폐 단위
     - 리턴
        양의 정수 금액 중 최솟값
"""
import sys

n = int(sys.stdin.readline().split()[0])  # n개의 동전
coins = list(map(int, sys.stdin.readline().split()))  # 동전들

coins.sort()

okay = 0  # 현재까지 가능한 수

for c in coins:
    if c <= okay + 1:  # 현재까지 가능한 수 + 1 보다 크거나 같은 경우, 동전을 만들 수 있음
        okay += c
    else:  # 현재까지 가능한 수 + 1 보다 작은 경우는 못만드는 경우
        break

print(okay + 1)
