"""
    부품찾기
5
8 3 7 9 2
3
5 7 9
"""
import sys


def search(array, target):
    """
    이진 탐색 함수
    """
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


n = int(sys.stdin.readline().split()[0])                # 매장에 존재하는 부품 수
my_list = list(map(int, sys.stdin.readline().split()))  # 매장에 존재하는 부품 번호
my_list.sort()  # 이진 탐색 전에 정렬

m = int(sys.stdin.readline().split()[0])                    # 손님이 요청한 부품 수
target_list = list(map(int, sys.stdin.readline().split()))  # 손님이 요청한 부품 번호

# 손님이 요청한 부품을 하나 씩 존재 여부 검토
for i in range(m):
    if search(my_list, target_list[i]):
        print("yes", end=" ")
    else:
        print("no", end=" ")
