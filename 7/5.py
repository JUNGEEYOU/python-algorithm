"""
    부품찾기

"""
import sys

def search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None

n = int(sys.stdin.readline().split()[0])
my_list = list(map(int, sys.stdin.readline().split()))
my_list.sort()

m = int(sys.stdin.readline().split()[0])
target_list = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    if search(my_list, target_list[i]):
        print("yes", end=" ")
    else:
        print("no", end=" ")


