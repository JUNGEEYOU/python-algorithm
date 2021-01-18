"""
    안테나
    https://www.acmicpc.net/problem/18310

"""
import sys

n = int(sys.stdin.readline().split()[0])
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print(arr[(n-1)//2])

