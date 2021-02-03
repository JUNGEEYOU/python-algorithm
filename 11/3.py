"""
  뒤집기
 https://www.acmicpc.net/problem/1439
 - 입력
    첫 줄 - s : 여러 개의 숫자로 구성된 하나의 문자열
 - 리턴
    첫째 줄에 만들어질 수 있는 가장 큰 수 출력

 02984
"""
import sys

s = str(sys.stdin.readline().split()[0])

count_0 = 0   # 0으로 바꿔야하는 경우
count_1 = 0   # 1로 바꿔야하는 경우

if s[0] == "0":
    count_1 += 1
else:
    count_0 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:  # 옆 문자와 다른 경우, 바뀌는 횟수 증가
        if s[i + 1] == "0":
            count_1 += 1
        else:
            count_0 += 1

print(min(count_1, count_0))