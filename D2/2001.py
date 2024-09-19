# 2001
# 파리 퇴치

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    fly = []
    for _ in range(N):
        fly.append(list(map(int, input().split())))
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(i,i+M):
                for l in range(j,j+M):
                    temp += fly[k][l]
                    
            if result < temp:
                result = temp 
    print("#"+str(test_case)+" "+str(result))
