# 1204
# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    scores = [0]*101
    num = int(input())
    record = list(map(int, input().split()))
    for i in range(len(record)):
        scores[record[i]] += 1
    max_score = max(scores)
    result = [j for j in range(len(scores)) if scores[j] == max_score]
    print(f"#{num} {result[-1]}")

