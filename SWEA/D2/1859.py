# 1859
# 백만 장자 프로젝트

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    price = list(map(int, input().split()))
    buying = 0
    profit = price[-1]
    for i in range(len(price)-2,-1,-1):
        if price[i] <= profit:
            buying += (profit - price[i])
        else:
            profit = price[i]
    print(f"#{test_case} {buying}")