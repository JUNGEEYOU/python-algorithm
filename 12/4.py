import copy


def rotate_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    mid_lock = [[0]*(n * 3) for _ in range(n * 3)]    # 중앙에 lock을 두기 위한 변수

    # 중앙에 lock 두기
    for i in range(n):
        for j in range(n):
            mid_lock[n + i][n + j] = lock[i][j]
    pre_lock = copy.deepcopy(mid_lock)
    for _ in range(4):      # 4방향을 돌면서
        key = rotate_90(key)
        for x in range(1, n * 2):
            for y in range(1, n * 2):
                # 키 넣기
                for i in range(m):
                    for j in range(m):
                        mid_lock[x + i][y + j] += key[i][j]
                if check(mid_lock):
                    return True
                mid_lock = copy.deepcopy(pre_lock)
    return False


print(solution(key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))