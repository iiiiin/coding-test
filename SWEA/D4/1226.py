# 1226
# [S/W 문제해결 기본] 7일차 - 미로1

'''
시작점, 도착점 찾기
시작점에서 델타 탐색을 이용한 BFS 수행
조건에 맞게 이동, 이동 후 도착하지 못할 경우 0 반환
'''

from collections import deque

# 시작점, 도착점 찾기
def find_point():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j

# 경로 탐색 (BFS)
def bfs(si, sj):
    q = deque([(si,sj)])
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if 0<=nr<16 and 0<=nc<16:
                if visited[nr][nc] == 0:
                    if arr[nr][nc] != 1:
                        if arr[nr][nc] == 3:
                            return 1
                        q.append((nr,nc))
                        visited[nr][nc] = 1

    return 0

delta = [(-1,0),(1,0),(0,-1),(0,1)]

for tc in range(1,11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    si, sj = find_point()
    print(f'#{t} {bfs(si,sj)}')