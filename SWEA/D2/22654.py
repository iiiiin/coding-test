# 22654
# 차윤이의 RC카

'''
구현
X를 찾고, X에서 시작
Y에 도착하는 지 확인
'''

def find_start():
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                return i, j

def go():
    ci, cj = si, sj
    d = 0
    for c in commands:
        if c == 'A':
            ni = ci + delta[d][0]
            nj = cj + delta[d][1]
            if 0<=ni<N and 0<=nj<N and field[ni][nj] != 'T':
                ci, cj = ni, nj
        elif c =='L':
            d = (d + 3) % 4
        elif c =='R':
            d = (d + 1) % 4
    if field[ci][cj] == 'Y':
        return 1
    else:
        return 0

T = int(input())

delta = [(-1,0),(0,1),(1,0),(0,-1)]

for tc in range(1,T+1):
    N = int(input())
    field = [input() for _ in range(N)]
    si, sj = find_start()
    Q = int(input())
    result = []
    for _ in range(Q):
        C, commands = input().split()
        result.append(go())

    print(f'#{tc}', *result)