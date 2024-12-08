# 11399
# ATM

import sys
input = sys.stdin.readline
n = int(input())
array = sorted(list(map(int, input().split())))
count = 0
for i in range(n):
    count += (array[i] * (n-i))
print(count)