"""
 전보

3 2 1
1 2 4
1 3 2
"""
import heapq
import sys

INF = int(1e9)

n, m, start = map(int, sys.stdin.readline().split())   # 노드 수, 간선 수, c 도시

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
result = 0
cost = 0
for i in range(1, n + 1):
    if distance[i] < INF:
        result += 1
        cost = max(cost, distance[i])

print(result - 1, cost)   # 시작노드는 제외