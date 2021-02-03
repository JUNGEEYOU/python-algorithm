"""
  곱하기 혹은 더하기

 - 입력
    첫 줄 - s : 여러 개의 숫자로 구성된 하나의 문자열
 - 리턴
    첫째 줄에 만들어질 수 있는 가장 큰 수 출력

 02984
"""
import sys
s = str(sys.stdin.readline().split()[0])   # 숫자로된 문자열

total = int(s[0])
for i in range(1, len(s)):
    if total == 0 or s[i] == 0:          # 앞에 값이 0이면 +
        total += int(s[i])
    else:                   # 아닌 경우 *
        total *= int(s[i])

print(total)

