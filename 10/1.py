"""
기본적인 구현 방법 - 문제: find할 때 o(v) 복잡도를 가질 수 있다.
6 4
1 4
2 3
2 4
5 6
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블 : 1 1 2 1 5 5
"""

import sys
def find_patent(parent, x):
    """
    특정 원소가 속한 집합 찾기 - find 연산
    :param parent:
    :param x:
    :return:
    """
    if parent[x] != x:
        return find_patent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    """
    두 원소가 속한 집합 합치기 - union 연산
    :param parent:
    :param a:
    :param b:
    :return:
    """
    a = find_patent(parent, a)
    b = find_patent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())    # 노드 개수, 간선 개수
parent = [0] * (v + 1)

for i in range(1, v + 1):   # 부모 테이블을 자기 자신으로 초기화
    parent[i] = i

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합:', end=' ')
for i in range(1, v + 1):
    print(find_patent(parent, i), end=' ')
print()

print('부모 테이블 :', end=' ')    # 루트 노드는 아닐 수 있음 - 그냥 부모
for i in range(1, v + 1):
    print(parent[i], end=' ')