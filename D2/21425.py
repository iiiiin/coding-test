# 21425
# +=

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    A, B, N = map(int, input().split())
    cnt = 0
    while A <= N and B <= N:
        if A < B:
            A += B
        elif A > B:
            B += A
        else:
            B += A
        cnt += 1
    print(cnt)