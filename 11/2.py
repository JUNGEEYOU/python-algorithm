"""
  곱하기 혹은 더하기

 - 입력
    첫 줄 - s : 여러 개의 숫자로 구성된 하나의 문자열
 - 리턴
    첫째 줄에 만들어질 수 있는 가장 큰 수 출력

 02984
"""
import sys
s = str(sys.stdin.readline().split()[0])
if len(s) == 1:
    print(s)
else:
    result = int(s[0])
    for i in range(1, len(s)):
        num = int(s[i])
        if num <= 1 or result <= 1:     # 앞 문자열이나 현재 문자열이 0 이거나 1이면 합하기
            result = result + int(s[i])
        else:
            result = result * int(s[i])

    print(result)

