# 1940
# 가랏! RC카!

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    current_speed = 0
    result = 0
    for i in range(n):
        rc = list(map(int, input().split()))
        if rc[0] == 1:
            current_speed += rc[1]
            result += current_speed
        elif rc[0] == 2:
            if current_speed < rc[1]:
                current_speed = 0
            else:
                current_speed -= rc[1]
            result += current_speed
        else:
            result += current_speed
    print(f"#{test_case} {result}")