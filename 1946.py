# 1946
# 간단한 압축 풀기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    result = ""
    for i in range(n):
        ci, ki = input().split()
        result += ci*int(ki)
    print(f"#{test_case}")
    for k in range(0,len(result),10):
        print(result[k:k+10])