# 9093
# 단어 뒤집기

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    s = input().split()
    for i in range(len(s)):
        if i == len(s)-1:
            print(s[i][::-1])
        else:
            print(s[i][::-1],end=' ')
