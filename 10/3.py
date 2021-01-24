"""
서로소 집합을 활용한 사이클 판별
3 3
1 2
1 3
2 3
사이클 존재
"""
import sys


def find_patent(parent, x):
    if parent[x] != x:
        parent[x] = find_patent(parent, parent[x])
    return parent[x]


def union_patent(parent, a, b):
    a = find_patent(parent, a)
    b = find_patent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())  # 노드 개수, 간선 개수
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    # 사이클이 발생한 경우 종료
    if find_patent(parent, a) == find_patent(parent, b):
        cycle = True
        break
    else:
        union_patent(parent, a, b)

if cycle:
    print("사이클 존재")
else:
    print("사이클 존재 x ")