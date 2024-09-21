# 1234
# [S/W 문제해결 기본] 10일차 - 비밀번호

import sys
sys.stdin = open("input.txt", "r", encoding="utf-8")

for test_case in range(1,11):
    n, digit = input().split()
    num = ["00","11","22","33","44","55","66","77","88","99"]
    while True:
        temp = digit
        for x in num:
            digit = "".join(digit.split(x))
        if temp == digit:
            break
    print(f"#{test_case} {digit}")