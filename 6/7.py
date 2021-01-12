"""
 1. sorted 함수 사용
"""
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)  # [0, 1, 2, 4, 5, 6, 7, 8, 9]

"""
 2. sort 메소드 사용 - 리스트 변수 
"""
array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

array.sort()
print(array)  # # [0, 1, 2, 4, 5, 6, 7, 8, 9]

"""
 3. key 매개변수 사용 - 함수 사용 + sorted 
"""
array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)  # [('바나나', 2), ('당근', 3), ('사과', 5)]
print(result)


"""
 4. sort함수 - 람다 
"""
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0])   # Stable Sort (When using a key)
print(data)
