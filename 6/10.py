"""
 두 배열의 원소 교체


5 3
1 2 5 4 3
5 5 6 6 5
"""
import sys
n, k = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

a_list.sort()             # 오름차순
b_list.sort(reverse=True) # 내림차순

for i in range(k):
    if a_list[i] < b_list[i]:
        a_list[i] = b_list[i]
    else:
        break

print(sum(a_list))


