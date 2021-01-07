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
data = str(sys.stdin.readline().split()[0])
count0 = 0    # 전부 0으로 바꾸는 경우
count1 = 0    # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))