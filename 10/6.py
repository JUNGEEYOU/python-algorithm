"""
    팀 결성

"""
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())  # 0~n개의 팀, m개의 연산

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())  # 연산 번호, a학생 b 학생
    if a == 0:  # 팀 합치기 - union
        union_parent(parent, b, c)
    else:  # 같은 팀 여부 확인 - find
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")
