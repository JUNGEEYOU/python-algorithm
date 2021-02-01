"""
    크루스칼 알고리즘
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

"""
import sys


def find_parent(parent, x):
    """
    자기가 속한 최종 부모 찾기
    :param parent:
    :param x:
    :return:
    """
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    """
    두 원소 합치기 - 부모 동일
    :param parent:
    :param a:
    :param b:
    :return:
    """
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())  # 노드 개수, 간선 개수
parent = [0] * (v + 1)

edges = []
result = 0

# 1. 부모 저장 테이블 - 자기 자신으로 세팅
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

# 2. 간선 그래프를 비용에 따른 오름차순으로 설정. 그리디 - 정렬 필요
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):   # 사이클 발생 안한 경우 합치기
        union_parent(parent, a, b)
        result += cost
print(result)  # 연결된 노드 최종 비용