# 1954
# 달팽이 숫자

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    x, y = 0, 0
    dir = 0
    snail = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n*n+1):
        if dir == 0:
            if y < n-1 and snail[x][y+1] != 0:
                dir += 1
                snail[x][y] = i
                x += 1
                continue
            elif y < n-1 and snail[x][y+1] == 0:
                snail[x][y] = i
                y += 1
            else:
                snail[x][y] = i
                dir += 1
                x += 1
                continue
        elif dir == 1:
            if x < n-1 and snail[x+1][y] != 0:
                dir += 1
                snail[x][y] = i
                y -= 1
                continue
            elif x < n-1 and snail[x+1][y] == 0:
                snail[x][y] = i
                x += 1
            else:
                snail[x][y] = i
                dir += 1
                y -= 1
                continue
        elif dir == 2:
            if y > 0 and snail[x][y-1] != 0:
                dir += 1
                snail[x][y] = i
                x -= 1
                continue
            elif y > 0 and snail[x][y-1] == 0:
                snail[x][y] = i
                y -= 1
            else:
                snail[x][y] = i
                dir += 1
                x -= 1
                continue
        elif dir == 3:
            if x > 0 and snail[x-1][y] != 0:
                dir = 0
                snail[x][y] = i
                y += 1
                continue
            elif x > 0 and snail[x-1][y] == 0:
                snail[x][y] = i
                x -= 1
            else:
                snail[x][y] = i
                dir = 0 
                y += 1
                continue
    print("#"+str(test_case))
    for i in range(n):
        print(*snail[i])