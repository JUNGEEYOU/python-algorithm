import sys

n = str(sys.stdin.readline().split()[0])
len_n = len(n)
sum_left = sum(map(int, n[0:(len_n//2)]))
sum_right = sum(map(int, n[(len_n//2):len_n]))
print("LUCKY" if sum_left == sum_right else "READY")