"""
    안테나
    https://www.acmicpc.net/problem/18310

"""
import sys

n = int(sys.stdin.readline().split()[0])    # 집의 수
loc = list(map(int, sys.stdin.readline().split()))   # 각 위치

loc.sort()

print(loc[(n - 1)//2])    # 중간 인덱스를 안테나로 잡기
