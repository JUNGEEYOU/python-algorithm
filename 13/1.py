"""
특정 거리의 도시 찾기
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
2 3
2 4

4 4 1 1
1 2
1 3
2 3
2 4

"""
import sys
from collections import deque


n, m, k, x = map(int, sys.stdin.readline().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)]
dis = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

que = deque()
que.append(x)
while que:
    b = que.popleft()
    for i in graph[b]:
        if dis[i] == 0 and i != x:      # 첫 도시는 또 방문하면 안됨!
            que.append(i)
            dis[i] = dis[b] + 1

count = 0
for i, d in enumerate(dis):
    if d == k:
        count += 1
        print(i)

if count == 0:
    print(-1)

