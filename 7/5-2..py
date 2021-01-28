"""
    부품찾기 - 집합 자료형
5
8 3 7 9 2
3
5 7 9
"""
import sys

n = int(sys.stdin.readline().split()[0])
my_list = set(map(int, sys.stdin.readline().split()))   # 집합 자료형 - 중복 제거

m = int(sys.stdin.readline().split()[0])
target_list = list(map(int, sys.stdin.readline().split()))

for t in target_list:
    if t in my_list:
        print("yes", end=" ")
    else:
        print("no", end=" ")

