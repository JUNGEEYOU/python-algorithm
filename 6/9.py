"""
 성적이 낮은 순서로 학생 출력하기

2
lena 100
jim 40
"""
import sys
n = int(sys.stdin.readline().split()[0])
array = list()
for _ in range(n):
    x, y = map(str, sys.stdin.readline().split())
    array.append((x, int(y)))

array.sort(key=lambda x: x[1])

for i in range(len(array)):
    print(array[i][0], end=" ")