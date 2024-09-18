# 1948
# 날짜 계산기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    month_end = [31,28,31,30,31,30,31,31,30,31,30,31]
    first_month, first_day, second_month, second_day = map(int, input().split())
    result = second_day - first_day + 1
    if second_month - first_month > 0:
        for i in range(first_month, second_month):
            result += month_end[i-1]
    print(f"#{test_case} {result}")