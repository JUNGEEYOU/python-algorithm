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
    # 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            # 2. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
            indegree[i] -= 1
            # 3. 새롭게 진입차수가 0이된 노드를 큐에 넣기
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()