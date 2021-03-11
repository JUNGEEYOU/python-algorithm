"""
7 2
1 1 2 2 2 2 3
4


"""
import bisect
import sys

def count_range(a, left, right):
    left = bisect.bisect_left(a, left)
    right = bisect.bisect_right(a, right)
    return right - left


n, x = map(int, sys.stdin.readline().split())   # n개의 원소, x의 정수
arr = list(map(int, sys.stdin.readline().split()))
res = count_range(arr, x, x)
if res:
    print(res)
else:
    print(-1)