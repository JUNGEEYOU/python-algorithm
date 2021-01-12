"""
 위에서 아래로

3
15
27
12
"""
import sys

n = int(sys.stdin.readline().split()[0])
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline().split()[0]))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')