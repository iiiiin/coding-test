# 14503
# 로봇 청소기

'''
구현
델타탐색
'''

import sys
input = sys.stdin.readline

# 북 -> 동 -> 남 -> 서
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 현재 칸 청소
arr[r][c] = 2
cnt = 1
new_d = d
while True:
    # 현재 칸이 청소되지 않은 경우 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    # 청소되지 않은 빈 칸이 있는 경우
    for _ in range(4):
        new_d = (new_d+3) % 4
        new_r, new_c = r + delta[new_d][0], c + delta[new_d][1]
        # 인덱스 범위 확인
        if 0<=new_r<N and 0<=new_c<M:
            # 청소되지 않은 빈 칸인 경우
            if arr[new_r][new_c] == 0:
                r, c, d = new_r, new_c, new_d
                break
    # 청소되지 않은 빈 칸이 없는 경우
    else:
        rear_d = (new_d + 2) % 4
        new_r, new_c = r + delta[rear_d][0], c + delta[rear_d][1]
        # 인덱스 범위 확인
        if 0 <= new_r < N and 0 <= new_c < M:
            # 후진 가능한 경우
            if arr[new_r][new_c] != 1:
                r, c = new_r, new_c
            else:
                break
print(cnt)



