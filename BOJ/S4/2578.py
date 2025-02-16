'''
오류 원인 : 
사회자가 수를 부를 때, 
한 번에 여러 빙고가 발생하는 경우를 고려하지 못하고,
3개일 때만 값을 반환하게 해서 발생

'''


# 2578
# 빙고

import sys
sys.stdin = open('input.txt','r')

# 함수 : 0,0 시작 대각선 확인
def check_diag_left(arr):
    for i in range(5):
        if arr[i][i] != 'x':
            return 0
    return 1

# 함수 : 4,0 시작 대각선 확인
def check_diag_right(arr):
    for i in range(5):
        if arr[i][4-i] != 'x':
            return 0
    return 1

# 함수 : 행과 열의 빙고 확인
def check_rows_n_cols(arr):
    cnt = 0
    # 행의 빙고 여부 확인
    for i in range(5):
        for j in range(5):
            if arr[i][j] != 'x':
                break
        else:
            cnt += 1
    # 열의 빙고 여부 확인
    for j in range(5):
        for i in range(5):
            if arr[i][j] != 'x':
                break
        else:
            cnt += 1
    return cnt

# 함수 : 전체 횟수 반환 함수
def check_total_bingo(bingo, host):
    # result = 부른 횟수
    result = 0
    for i in range(5):
        for j in range(5):
            result += 1
            for k in range(5):
                for l in range(5):
                    if host[i][j] == bingo[k][l]:
                        bingo[k][l] = 'x'
                    if check_diag_left(bingo)+check_diag_right(bingo)+check_rows_n_cols(bingo) >= 3:
                        return result
    return result
                

# 빙고판 입력 받기
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자 입력 받기 
host = [list(map(int, input().split())) for _ in range(5)]

print(check_total_bingo(bingo,host))




        