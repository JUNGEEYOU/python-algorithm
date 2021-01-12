"""
선택 정렬
"""

def selection_sort(a):
    """
    선택 정렬 함수
    :param a: 리스트
    :return:
    """
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]
    print(a)


array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
selection_sort(array)