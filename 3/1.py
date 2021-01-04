"""
현재 카운터에 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정했을 때,
손님에게 거슬러줘야 할 돈이 N원이라면, 거슬러 줘야 할 동전의 최소 개수를 구하라. N = 1260 이라고 가정하자
"""

coin = [500, 100, 50, 10]
N = 1260
count = 0

for c in coin:
    count += N // c
    N %= c
print(count)