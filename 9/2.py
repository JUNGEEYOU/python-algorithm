import heapq
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())   # 노드 수, 간선 수
start = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())   # a => b 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # 시작 노드 거리를 0으로 설정
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:   # 처리된적 있으면 무시
            continue
        for i in graph[now]:   # 인접 노드 확인
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