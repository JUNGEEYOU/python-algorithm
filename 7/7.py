from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
target = 4

print(bisect_left(a, target))     # 2
print(bisect_right(a, target))    # 4