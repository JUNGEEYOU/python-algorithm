from collections import deque

def solution(board):
    """
    로봇은 (1, 1), (1, 2)에 존재한다. 
     (N, N)에 도착하여 걸리는 최소 시간
    :param board:
    :return:
    """
    answer = 0
    # 상하 좌우 이동을 위한
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = len(board)
    result = 0
    queue = deque()
    queue.append((0, 0, 0, 1))
    visited = {(0, 0), (0, 1)}
    while queue:
        x0, y0, x1, y1 = queue.popleft()
        # 상하좌우 움직이기
        for a in range(4):
            nx0, ny0, nx1, ny1 = dx[a] + x0, dy[a] + y0, dx[a] + x1, dy[a] + y1
            # 범위에 존재
            if nx0 < 0 or ny0 < 0 or nx0 >= n or ny0 >= n or nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= n:
                continue
            # 0이 아닌 경우
            if board[nx0][ny0] == 0 and board[nx1][ny1] != 0:
                continue
            # 처음 방문하는 경우
            if {(nx0, ny0), (nx1, ny1)} not in visited:
                queue.append((nx0, ny0, nx1, ny1))
                visited.add({(nx0, ny0), (nx1, ny1)})
        # 회전하기
        if y1 == y0:    # 세로 방향인 경우
            for i in [-1, 1]:   # 왼쪽 이동, 오른쪽이동
                if board[x0 + i][y0 + i] != 0 or board[x1 + i][y1 + i] != 0:   # 해당 위치에 0이면 회전 가능
                    continue
                if {(x0, y0), (x1, y1 + i)} not in visited and {(x1, y1), (x1, y1 + i)} not in visited:
                    queue.append(x0, y0, x0, y0 + i)
                    queue.append(x1, y1, x1, y1 + i)
                    visited.add({(x0, y0), (x1, y1 + i)})
                    visited.add({(x1, y1), (x1, y1 + i)})

        elif x0 == x1:  # 가로 방향인 경우
            for i in [-1, 1]:  # 위, 아래
                if board[x0 + i][y0 + i] != 0 or board[x1 + i][y1 + i] != 0:  # 해당 위치에 0이면 회전 가능
                    continue
                if {(x0, y0), (x1 + i, y1)} not in visited and {(x0, y0), (x1 + i, y1)} not in visited:
                    queue.append(x0, y0, x0 + i, y0)
                    queue.append(x1, y1, x1 + i, y1)
                    visited.add({(x0, y0), (x1 + i, y1)})
                    visited.add({(x1, y1), (x1 + i, y1)})

    return answer


print(solution(board=[[0, 0, 0, 1, 1],
                      [0, 0, 0, 1, 0],
                      [0, 1, 0, 1, 1],
                      [1, 1, 0, 0, 1],
                      [0, 0, 0, 0, 0]]))