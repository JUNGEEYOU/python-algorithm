"""
    부품찾기 - 계수 정렬
5
8 3 7 9 2
3
5 7 9
"""
import sys

array = [0] * 1000001

n = int(sys.stdin.readline().split()[0])
# 가게에 있는 경우 1로 설정
for i in sys.stdin.readline().split():
    array[int(i)] = 1

m = int(sys.stdin.readline().split()[0])
target_list = list(map(int, sys.stdin.readline().split()))

for i in target_list:
    if array[i]:   # 1인 경우는 가게에 있는 상태
        print("yes", end=" ")
    else:
        print("no", end=" ")
