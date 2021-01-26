"""
 큰 수의 법칙
 N개의 자연수 리스트, M 개의 수를 선택, K 만큼 연속 가능.
 가장 큰 수를 리턴한다.

 예시 입력
 5 8 3
 2 4 5 4 6
"""
import sys


n, m, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort(reverse=True)

temp = (array[0] * k) + array[1]

a = m // (k + 1)   # 해당 만큼은 묶음으로 반복
b = m % (k + 1)    # 나머지는 가장 큰 수로 채움

print(temp*a + array[0]*b)



