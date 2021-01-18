import bisect
def binary_search(array=list(), target=int()):
    """
    이진 탐색 -  bisect
    :param array:
    :param target:
    :return: target index
    """
    index = bisect.bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return index
    return None


array=[-1, 0, 3, 5, 9, 12]
print(binary_search(array=array, target=9))