"""
    만들 수 없는 금액
    - 입력
        첫 줄 - n : 동전의 개수
        둘째 줄 : 화폐 단위
     - 리턴
        양의 정수 금액 중 최솟값
"""
import sys
n = int(sys.stdin.readline()[0])
coins = list(map(int, sys.stdin.readline().split()))
coins.sort(reverse=False)
result = 0
for c in coins:
    pass
