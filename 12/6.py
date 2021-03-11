def check(answer):
    for x, y, a in answer:
        if a == 0:   # 기둥인 경우, 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야함
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        else:      # 보인 경우, 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x + 1, y, 1] in answer and [x - 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame: # (x, y), a(0: 기둥, 1: 보), b(0: 삭제, 1: 설치)
        if b == 1:     # 설치하는 경우
            answer.append([x, y, a])
            if not check(answer):    #  불가능한 경우, 삭제
                answer.remove([x, y, a])
        else:     # 삭제하는 경우
            answer.remove([x, y, a])
            if not check(answer):    #  불가능한 경우, 재 설치
                answer.append([x, y, a])

    return sorted(answer, key=lambda i: (i[0], i[1], i[2]))


print(solution(n=5, build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))