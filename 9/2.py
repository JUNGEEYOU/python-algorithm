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
import heapq
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())  # 노드 수, 간선 수
start = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())  # a => b 비용 c
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 1. 시작 노드 거리를 0으로 설정
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 2. 방문하지 않은 노드 중 짧은 노드 선택
        if distance[now] < dist:  # 처리된적 있으면 무시
            continue
        # 3. 현재 선택된 노드를 거쳐가는 비용을 계산하여 최단 거리 테이블 갱신
        for i in graph[now]:  # 인접 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
