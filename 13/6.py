import sys
import itertools
import copy

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline().split()[0])   # n*n
arr = []
x_arr = []
t_arr = []
s_arr = []
for i in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    x = [(i, j) for j in range(len(a)) if a[j] == "X"]
    t = [(i, j) for j in range(len(a)) if a[j] == "T"]
    s = [(i, j) for j in range(len(a)) if a[j] == "S"]
    if x: x_arr.extend(x)
    if t: t_arr.extend(t)
    if s: s_arr.extend(s)
    arr.append(a)

temp_arr = copy.deepcopy(arr)


def dfs(arr, x, y, idx):
    global n
    if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] == 'O':
        return
    else:
        arr[x][y] = 'T'
        dfs(arr, x + dx[idx], y + dy[idx], idx)

for c in itertools.combinations(x_arr, 3):
    flag = True
    for a, b in c:
        arr[a][b] = 'O'
    for x, y in t_arr:      # 선생님을 dfs로 감시 진행
        for i in range(4):
            dfs(arr, x, y, i)
    for x, y in s_arr:
        if arr[x][y] != 'S':     # 학생이 아닌 사람이 있는 경우 > 실패
            flag = False
    if flag:     # 학생 모두가 있는 경우
        break
    arr = copy.deepcopy(temp_arr)

if flag:
    print("YES")
else:
    print("NO")

