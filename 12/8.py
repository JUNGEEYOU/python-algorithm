import itertools


def solution(n, weak, dist):
    """
    :param n: 외벽의 둘레
    :param weak:  취약점 위치
    :param dist:  친구들의 이동 가능 거리
    :return:  최소 친구 수
    """
    answer = len(dist)
    week_len = len(weak)
    # 원형을 2배로 만들기
    double_weak = weak + [w + n for w in weak]

    for i, start in enumerate(weak):
        for ps in itertools.permutations(dist, len(dist)):
            count = 1
            position = start
            for p in ps:
                position += p
                # 현재 위치가 끝까지 못 갔을 경우
                if position < double_weak[i + week_len - 1]:
                    count += 1
                    position = [w for w in double_weak[i+1:i+week_len] if w > position][0]
                else:
                    answer = min(answer, count)
                    break

    if answer == float("inf"):
        return -1
    return answer
print(solution(n=12, weak=[1, 5, 6, 10], dist=[1, 2, 3, 4]))