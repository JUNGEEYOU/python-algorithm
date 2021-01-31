"""
 미래 도시
 1번 ~ k ~ x 도착
 => 우선 1~k까지 k에서 x까지 거리 구하기?

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
3

4 2
1 3
2 4
3 4
-1
"""
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())   # 전체 회사 개수, 경로 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, sys.stdin.readline().split())


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
