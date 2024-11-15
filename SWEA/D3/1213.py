# 1213
# [S/W 문제해결 기본] 3일차 - String

import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")


for test_case in range(1,11):
    n = int(input())
    s_find = input()
    s = input()
    i = 0
    result = 0
    while i <= len(s) - 1:
        if s[i:i+len(s_find)] == s_find:
            result += 1
            i += len(s_find)
        else:
            i += 1
    print(f"#{n} {result}")