# 10816
# 숫자 카드 2

import sys
input = sys.stdin.readline
a = int(input())
N = sorted(map(int,input().split()))
b = int(input())
M = map(int,input().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = a - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))

# 10816 - 숫자 카드 2 - Counter

# from math import inf
# from collections import Counter

# n = int(input())
# a = Counter(list(map(int, input().split())))
# m = int(input())
# array = list(map(int, input().split()))
# c = []
# for i in range(m):
#     if array[i] in a:
#         c.append(a[array[i]])
#     else:
#         c.append(0)
# for i in range(m):
#     print(c[i], end=' ')