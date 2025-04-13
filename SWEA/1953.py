# 1953
# [모의 SW 역량테스트] 탈주범 검거

'''
터널 구조물마다 어떻게 이동할 것인지 결정
현재 구조물에서 이동할 수 있는 방향과 이동할 방향에서 이동할 수 있는 방향이
연결될 수 있는지 확인 => 방향에 음수취한 값이 존재할 경우
현재위치에서 이동할 수 있는 경우를 모두 큐에 추가하여 같은 레벨로 체크 => BFS
'''

from collections import deque

T = int(input())

structures = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


def bfs(si, sj, aisle):
    q = deque([(si, sj, aisle)])
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    while q:
        cr, cc, ca = q.popleft()
        for dr, dc in structures[ca]:
            nr = cr + dr
            nc = cc + dc
            # 인덱스 확인
            if 0 <= nr < N and 0 <= nc < M:
                # 방문 확인
                if not visited[nr][nc]:
                    # 이동가능 여부 확인
                    na = tunnels[nr][nc]
                    if na != 0 and (-dr, -dc) in structures[na]:
                        # 이동
                        q.append((nr, nc, na))
                        visited[nr][nc] = visited[cr][cc] + 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    return cnt


for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnels = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(R, C, tunnels[R][C])}')
