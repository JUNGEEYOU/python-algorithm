from typing import List

def quick_sort(a:List) -> List:
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        low = [x for x in a[1:] if x <= pivot]
        high = [x for x in a[1:] if x > pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)

array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
print(quick_sort(array))