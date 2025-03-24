# 14888
# 연산자 끼워넣기

'''
DFS
'''

import sys
input = sys.stdin.readline

def dfs(idx, temp, plus, minus, multiple, divide):
    global min_v, max_v
    if idx == N:
        min_v = min(min_v, temp)
        max_v = max(max_v, temp)
        return

    if plus > 0:
        dfs(idx + 1, temp + operand[idx], plus - 1, minus, multiple, divide)
    if minus > 0:
        dfs(idx + 1, temp - operand[idx], plus, minus - 1, multiple, divide)
    if multiple > 0:
        dfs(idx + 1, temp * operand[idx], plus, minus, multiple - 1, divide)
    if divide > 0:
        dfs(idx + 1, int(temp / operand[idx]), plus, minus, multiple, divide - 1)


N = int(input())
operand = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
min_v, max_v = float('inf'), float('-inf')
dfs(1, operand[0], plus, minus, multiple, divide)
print(max_v, min_v, sep='\n')
