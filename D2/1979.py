# 1979
# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    n, k = map(int, input().split())
    puzzle = []
    result = 0
    for _ in range(n):
        puzzle.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n-k+1):
            if j == 0 and puzzle[i][j+k] == 0:
                if 0 not in puzzle[i][j:j+k]:
                    result += 1
            elif j == n - k and puzzle[i][j-1] == 0:
                if 0 not in puzzle[i][j:j+k]:
                    result += 1
            elif j != 0 and j != n-k:
                if puzzle[i][j-1] == 0 and puzzle[i][j+k] == 0:
                    if 0 not in puzzle[i][j:j+k]:
                        result += 1
    t_puzzle = list(map(list, zip(*puzzle)))
    for i in range(n):
        for j in range(n-k+1):
            if j == 0 and t_puzzle[i][j+k] == 0:
                if 0 not in t_puzzle[i][j:j+k]:
                    result += 1
            elif j == n - k and t_puzzle[i][j-1] == 0:
                if 0 not in t_puzzle[i][j:j+k]:
                    result += 1
            elif j != 0 and j != n-k:
                if t_puzzle[i][j-1] == 0 and t_puzzle[i][j+k] == 0:
                    if 0 not in t_puzzle[i][j:j+k]:
                        result += 1
    print(f"#{test_case} {result}")