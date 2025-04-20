# 11559
# Puyo Puyo

'''
블록찾기
터지는 지점들을 모두 찾아 큐에 삽입
상하좌우로 BFS를 수행하여 방문처리 (제거)
바이러스처럼 퍼져나가지 않고, 단순히 지점을 세어 값을 바꾸는 것이므로
1. 배열을 순회하면서 BFS를 수행가능
2. 그리고 블록내림 수행
3, 1번 과정 반복 (횟수 + 1)
4. flag로 제거를 수행한 지 확인하여 변화가 없었다면 종료
'''

from collections import deque

import sys
input = sys.stdin.readline

# 블록 제거 함수
def boom(si, sj):
    spot = []
    visited = [[0] * 6 for _ in range(12)]
    q = deque([(si,sj)])
    spot.append((si,sj))
    visited[si][sj] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<12 and 0<=nc<6:
                if arr[nr][nc] == arr[r][c]:
                    if visited[nr][nc] == 0:
                        spot.append((nr,nc))
                        q.append((nr,nc))
                        visited[nr][nc] = 1
    if len(spot) >= 4:
        for i, j in spot:
            arr[i][j] = '.'
        return 1

    return 0

# 블록 내림 함수
def down():
    global arr
    temp = list(map(list, zip(*arr)))
    for idx in range(6):
        unempty = ''.join([x for x in temp[idx] if x != '.'])
        temp[idx] = '.'*(12-len(unempty)) + unempty
    arr = list(map(list, zip(*temp)))

arr = [list(input()) for _ in range(12)]
cnt = 0
while True:
    flag = 0
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                flag += boom(i,j)
    if flag == 0:
        break
    cnt += 1
    down()
print(cnt)


