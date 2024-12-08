# 1018
# 체스판 다시 칠하기

n, m = map(int, input().split())
array = [list(input()) for i in range(n)]
count = []
for x in range(n-7):
    for y in range(m-7):
        w_idx = 0
        b_idx = 0
        for i in range(x,x+8):
            for j in range(y,y+8):
                if (i+j) % 2 == 0:
                    if array[i][j] != 'W':
                        w_idx += 1
                    else:
                        b_idx += 1
                else:
                    if array[i][j] != 'W':
                        b_idx += 1
                    else:
                        w_idx += 1
        count.append(w_idx)
        count.append(b_idx)
print(min(count))