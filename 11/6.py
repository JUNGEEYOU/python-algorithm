"""
 무지의 먹방 라이브
 왜 3번케이스?
"""
def solution(food_times, k):
    index = 0
    n = len(food_times)
    if sum(food_times) <= k:
        return -1
    while k:
        k -= 1
        if food_times[index] > 0:
            food_times[index] -= 1
        else:
            k += 1
        index = (index + 1) % n
    return index + 1


print(solution(food_times=[3, 1, 2], k=5))