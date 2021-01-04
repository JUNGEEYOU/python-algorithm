"""
 숫자 카드 게임
 n : 행의 개수 m: 열의 개수
 n개의 줄에 걸친 각 카드 숫자
 - 출력: 게임 룰에 맞는 선택된 카드
 하나의 행을 선택해서 가장 작은 수의 카드를 뽑는다. 이때 가장 큰 수를 뽑기위한 전략

 예시 입력
    3 3
    3 1 2
    4 1 4
    2 2 2

    2 4
    7 3 1 8
    3 3 3 4
"""
import sys

n, m = map(int, sys.stdin.readline().split())
result = 1
for _ in range(n):
    card = list(map(int, sys.stdin.readline().split()))
    min_val = min(card)
    result = max(result, min_val)

print(result)