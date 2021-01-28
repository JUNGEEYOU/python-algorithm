from collections import deque

# 네 방향으로 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = 4, 3  # 세로, 가로
graph = [
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 1]
    ]

visited = [[False] * m for _ in range(n)]   # 방문 유무
count = 0   # 섬의 수

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            count += 1
            while queue:
                x, y = queue.popleft()
                print(x, y)
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny] or not graph[nx][ny]:
                        continue
                    queue.append((nx, ny))
                    visited[nx][ny] = True
print(count)