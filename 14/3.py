"""
    실패율
    https://programmers.co.kr/learn/courses/30/lessons/42889
"""
def solution(n, stages):
    answer = []
    count = [0] * (n + 1)
    num = 0
    for stage in stages:
        if stage > n:
            num += 1
        else:
            count[stage] += 1

    for i in range(n, 0, -1):
        num += count[i]
        if num == 0:
            answer.append((i, 0))
        else:
            answer.append((i, (count[i]/num)))

    answer.sort(key=lambda a: (a[1], -a[0]), reverse=True)

    return [a[0] for a in answer]

print(solution(n=4, stages=[4,4,4,4,4]))
