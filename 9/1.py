"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""


import sys

INF = int(1e9)     # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, sys.stdin.readline().split())   # 노드 수, 간선 수

start = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())   # a => b 비용 c
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):    # 가장 작은 노드를 찾기 위해 완전탐색
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:    # 시작노드 인접한 노드에 자기 자신 비용 넣기
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()    # 가장 잛은 거리를 가진 노드 찾기
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]         # 인접한 노드 비용 + 내 비용
            if cost < distance[j[0]]:           # 비용 < 인접 노드의 현재 비용 - 갱신
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
