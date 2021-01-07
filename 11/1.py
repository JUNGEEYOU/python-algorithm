"""
 모험자 길드

 - 입력
    첫 줄 - n: 모험가 수
    둘째 줄 : 모험가의 공포도
 - 리턴
    여행을 떠날 수 있는 그룹의 최댓값

5
2 3 1 2 2
"""
import sys
n = int(sys.stdin.readline().split()[0])
data = list(map(int, sys.stdin.readline().split()))
data.sort()
count = 0    # 사람 수
result = 0   # 그룹 수
for d in data:
    count += 1
    if d <= count:
        result += 1
        count = 0
print(result)

