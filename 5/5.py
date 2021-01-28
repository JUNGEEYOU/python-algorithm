"""
 dfs(재귀) - '1' 노드 방문 & 독립된 노드 수 확인
"""
n, m = 4, 3  # 세로, 가로
graph = [
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 0, 0]
    ]

visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or visited[x][y] or not graph[x][y]:
        return False
    visited[x][y] = True
    print(x, y)
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)