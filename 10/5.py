"""
 위상 정렬 알고리즘

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
1 2 5 3 6 4 7
"""
from collections import deque
import sys


v, e = map(int, sys.stdin.readline().split())  # 노드 수, 간선 수

indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # a > b
    indegree[b] += 1    # 진입 차수

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:  # 처음은 진입차수가 0인 것부터. 진입차수 0이 시작하는 노드이기 때문
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:   # 인접 노드 진입 차수 -1 & 0이면 큐에 넣기
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()