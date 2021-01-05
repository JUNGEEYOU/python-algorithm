"""
 시각
 - 입력
    첫 줄 - N : 00시 00분 00초 ~ n시 59분 59초
 - 리턴
    3이 하나라도 포함되어 있는 경우의 수를 출력
"""
import sys
n = int(sys.stdin.readline())
result = 0
for s in range(0, n + 1):
    for m in range(0, 60):
        for n in range(0, 60):
            if '3' in str(s) + str(m) + str(n):
                result += 1
print(result)