"""
  럭키 스트레이트
    https://www.acmicpc.net/problem/18406
"""
import sys


def sum_list(n_list):
    result = 0
    for n in n_list:
        result += int(n)
    return result


n = str(sys.stdin.readline().split()[0])

n_1 = n[:(len(n) // 2)]
n_2 = n[(len(n) // 2):]
if sum_list(n_1) == sum_list(n_2):
    print("LUCKY")
else:
    print("READY")
