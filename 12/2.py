"""
  문자열 재정렬
  K1KA5CB7
"""
import sys

n = str(sys.stdin.readline().split()[0])
alpha = ''
num = 0
for c in n:
    if c.isalpha():
        alpha += c
    else:
        num += int(c)

alpha = ''.join(sorted(alpha))
print(alpha + str(num))