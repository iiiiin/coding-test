# 1931
# 회의실 배정

import sys
input = sys.stdin.readline
n = int(input())
array = sorted([list(map(int, input().split())) for x in range(n)], key=lambda x : (x[1],x[0]))
count = 1
k = array[0]
for i in range(1, len(array)):
    if array[i][0] >= k[1]:
        k = array[i]
        count += 1
print(count)