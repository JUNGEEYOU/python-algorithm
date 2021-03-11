import bisect

def count_by_range(a, left_val, right_val):
    """
    범위에 존재하는 데이터 개수
    """
    right_val = bisect.bisect_right(a, right_val)
    left_val = bisect.bisect_left(a, left_val)
    return right_val - left_val

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    # 단어를 정렬
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for querie in queries:
        if querie[0] == "?":    # 앞에 ?인 경우, ????o
            res = count_by_range(reversed_arr[len(querie)], querie[::-1].replace('?', 'a'), querie[::-1].replace('?', 'z'))
        else:                  # 뒤가 ?인 경우, fro??
            res = count_by_range(arr[len(querie)], querie.replace("?", "a"), querie.replace("?","z"))
        answer.append(res)
    return answer

print(solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"], queries=["fro??", "????o", "fr???", "fro???", "pro?"]))