# 1284
# 수도 요금 경쟁

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    water_p = W*P
    if W <= R:
        water_q = Q
    else:
        water_q = Q + (W-R)*S
    result = min(water_p, water_q)
    print(f"#{test_case} {result}")
