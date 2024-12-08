# 13305
# 주유소

import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
total = cost[0]*dist[0]
min_cost = cost[0]
for i in range(1,n-1):
    if min_cost >= cost[i]:
        min_cost = cost[i]
    total += min_cost*dist[i]
print(total)