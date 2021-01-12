"""
 계수 정렬(counting sort)
"""

array = [7, 5, 9, 0, 1, 6, 2, 4, 8, 0, 3, 3]
count = [0] * (max(array) + 1)

for a in array:
    count[a] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')