"""
 연산자 끼워넣기
"""
import sys
import itertools
min_result = float("inf")
max_result = float("-inf")
n = int(sys.stdin.readline().split()[0])  # 수의 개수
array = list(map(int, sys.stdin.readline().split()))  # 수
cal = list(map(int, sys.stdin.readline().split()))    # 덧셈, 뺄셈, 곱셈, 나눗셈 개수
cal_list = list()
for i, c in enumerate(cal):
    if c > 0:
        cal_list.extend([i] * c)
prn = itertools.permutations(cal_list, n - 1)
for c in prn:
    result = array[0]
    for a, b in zip(array[1:], c):
        if b == 0:
            result += a
        elif b == 1:
            result -= a
        elif b == 2:
            result = result * a
        else:
            if result < 0:
                result = abs(result)
                result = result // a
                result = - result
            else:
                result = result // a
    min_result = min(min_result, result)
    max_result = max(max_result, result)
print(max_result)
print(min_result)