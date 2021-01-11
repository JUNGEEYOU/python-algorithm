"""
bfs - 인접 리스트
"""
from collections import deque


def bfs(graph, visited, start):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:   # 큐에 넣고 방문 처리
                que.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)
bfs(graph, visited, 1)