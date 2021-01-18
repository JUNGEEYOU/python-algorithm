def binary_search(array=list(), target=int(), left=int(), right=int()):
    """
    이진 탐색 - 재귀 함수 구현
    :param array:
    :param target:
    :param left:
    :param right:
    :return: target index
    """
    if left > right:
        return None
    mid = (left + right) // 2     # 중간값. 몫
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array=array, target=target, left=mid + 1, right=right)
    else:
        return binary_search(array=array, target=target, left=left, right=mid - 1)

array=[-1, 0 , 3, 5, 9, 12]     # 정렬된 리스트!

result = binary_search(array=array, target=9, left=0, right=len(array) - 1)
if result:
    print(result)
else:
    print("없다.")