# 1974
# 스도쿠 검증

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    sudoku = []
    result = 1
    for j in range(9):
        sudoku.append(list(map(int, input().split())))
    
    # 가로, 세로 확인
    for p in range(9):
        ver = []
        hor = []
        for q in range(9):
            if sudoku[p][q] not in hor:
                hor.append(sudoku[p][q])
            else:
                result = 0
                break
            if sudoku[q][p] not in ver:
                ver.append(sudoku[q][p])
            else:
                result = 0
                break
    
    # 3x3 확인
    if result == 1:
        for p in range(0,9,3):
            for q in range(0,9,3):
                comp = []
                for r in range(3):
                    for s in range(3):
                        if sudoku[p+r][q+s] not in comp:
                            comp.append(sudoku[p+r][q+s])
                        else:
                            result = 0
                            break
        
    print("#"+str(test_case)+" "+str(result))