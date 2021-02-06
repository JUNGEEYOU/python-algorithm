"""
 무지의 먹방 라이브
 왜 3번케이스?
"""
import heapq

def solution(food_times, k):
    array = []
    if sum(food_times) <= k:
        return -1
    # 1. 힙큐에 삽입
    for i, time in enumerate(food_times):
        if time > 0:
            heapq.heappush(array, (time, (i + 1)))
    temp = 0    # 몇 바퀴 돌린지 변수
    # 한 번에 한 묶음 씩 제거하기
    while (len(array) * (array[0][0] - temp)) <= k:   # (전체 길이에서 * 가장 작은 시간) <= 남은 시간
        length = len(array)
        now = heapq.heappop(array)
        k -= ((now[0] - temp) * length)
        temp = now[0]
        while array[0][0] == now[0]:
            heapq.heappop(array)

    result = sorted(array, key=lambda x: x[1])   # 다시 인덱스 기준으로 정렬
    return result[k % len(array)][1]