"""
 연구소. https://www.acmicpc.net/problem/14502


"""
import sys
n, m = map(int, sys.stdin.readline().split())  # 세로 가로
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

