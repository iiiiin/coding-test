# 10157
# 자리배정

'''
달팽이 숫자
최종적으로 1부터 얼마까지의 수를 입력할 것인지
그만큼 반복문 수행
그리고 조건에 따라 방향을 변경하면서 입력
'''

import sys
input = sys.stdin.readline

C, R = map(int, input().split())
N = int(input())
# R*C 크기 0 배열 생성
arr = [[0] * C for _ in range(R)]
# 델타 배열
delta = [(-1,0),(0,1),(1,0),(0,-1)]
# 시작 방향
d = 0
# 시작 위치
r, c = R-1, 0
# 정답
answer = 0
# for문으로 하나씩 채우면서, N이 나온다면 반환 후 break
for i in range(1, R*C+1):
    arr[r][c] = 1
    # N이 나올 경우
    if i == N:
        answer = f'{c+1} {R-r}'
        break
    nr = r + delta[d][0]
    nc = c + delta[d][1]

    # 위로 가던 중 모두 채운 경우, 방향 전환
    if d == 0:
        if nr < 0:
            d = 1
        elif arr[nr][nc] != 0:
            d = 1
        r += delta[d][0]
        c += delta[d][1]
    # 오른쪽으로 가던 중 모두 채운 경우, 방향 전환
    elif d == 1:
        if nc > C-1:
            d = 2
        elif arr[nr][nc] != 0:
            d = 2
        r += delta[d][0]
        c += delta[d][1]
    # 아래로 가던 중 모두 채운 경우, 방향 전환
    elif d == 2:
        if nr > R-1:
            d = 3
        elif arr[nr][nc] != 0:
            d = 3
        r += delta[d][0]
        c += delta[d][1]
    # 왼쪽으로 가던 중 모두 채운 경우, 방향 전환
    elif d == 3:
        if nc < 0:
            d = 0
        elif arr[nr][nc] != 0:
            d = 0
        r += delta[d][0]
        c += delta[d][1]
# 찾지 못했다면 초기값 0 반환
# 반환한 값 출력

print(answer)