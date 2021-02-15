import sys
import itertools

n, m = map(int, sys.stdin.readline().split())   # n*n 도시, 최대 m개의 도시
graph = []
chicken = []
home = []
for i in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    search_chicken = [(i, j) for j, a in enumerate(array) if a == 2]
    search_home = [(i, j) for j, a in enumerate(array) if a == 1]

    if search_chicken:
        chicken.extend(search_chicken)
    if search_home:
        home.extend(search_home)

    graph.append(array)

result = float("inf")
ncr = itertools.combinations(chicken, m)   # 조합으로 경우의 수 찾기
for i in itertools.combinations(chicken, m):
    result_sum = 0
    for j in home:       # 각 집 리스트 마다 거리 찾기
        min_chicken = float("inf")
        for k in i:
            min_chicken = min(min_chicken, abs(k[0] - j[0]) + abs(k[1] - j[1]))
        result_sum += min_chicken
    result = min(result, result_sum)

print(result)
