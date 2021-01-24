def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

array = ["hanul", "jonggu", "dongbin", "taeil", "sangwook"]
print(sequential_search(len(array), "dongbin", array))    # 3 출력 