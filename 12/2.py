"""
  문자열 재정렬
  K1KA5CB7
"""
import sys
s = sys.stdin.readline().split()[0]
al_s = ''
num_s = 0
for c in s:
    if c.isalpha():
        al_s += c
    else:
        num_s += int(c)
al_s_sort = ''.join(sorted(al_s))

if num_s:
    print(al_s_sort + str(num_s))
else:
    print(al_s_sort)