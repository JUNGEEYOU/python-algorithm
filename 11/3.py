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

zero = 0
one = 0

if s[0] == "0":
    zero += 1
else:
    one += 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:  # 옆 문자와 다른 경우, 바뀌는 횟수 증가
        if s[i] == "0":
            zero += 1
        else:
            one += 1

print(min(zero, one))