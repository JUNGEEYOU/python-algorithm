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
coins.sort()

target = 1    # 1부터 target -1까지 가능
for c in coins:
    if target < c:  # target 못만드는 경우
        break
    target += c

print(target)
