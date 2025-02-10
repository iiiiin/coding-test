# 1210
# [S/W 문제해결 기본] 2일차 - Ladder1

for tc in range(1,11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, arr[99].index(2)
    dr = [-1, 0, 0]
    dc = [0, 1, -1]
    i = 0
    while r > 0:
        if i != 1 and c - 1 >= 0 and arr[r][c-1] == 1:
            i = 2
        elif i != 2 and c + 1 < 100 and arr[r][c+1] == 1:
            i = 1
        else:
            i = 0
        r = r + dr[i]
        c = c + dc[i]
    
    print(f'#{t} {c}')