def binary_search(array=list(), target=int()):
    """
    이진 탐색 -  반복문
    :param array:
    :param target:
    :return: target index
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

array=[-1, 0 , 3, 5, 9, 12]

result = binary_search(array=array, target=9)
if result:
    print(result)
else:
    print("없다")