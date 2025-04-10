# 2206
# 벽 부수고 이동하기

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 각 셀에 도달할 때 사용한 최소 벽 부순 횟수(0, 1) 저장
    visited = [[float('inf')] * M for _ in range(N)]
    q = deque()
    # (행, 열, 벽 부순 횟수)
    q.append((0, 0, 0))
    visited[0][0] = 0
    cnt = 1
    while q:
        for _ in range(len(q)):
            r, c, broken = q.popleft()
            if r == N - 1 and c == M - 1:
                return cnt

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    next_broken = broken
                    if grid[nr][nc] == 1:
                        # 만약 아직 벽을 부수지 않은 상태라면
                        if broken == 0:
                            next_broken = 1
                        else:
                            continue
                    # 더 적은 벽 부순 횟수로 이 칸에 도달한 경우
                    if visited[nr][nc] > next_broken:
                        visited[nr][nc] = next_broken
                        q.append((nr, nc, next_broken))
        cnt += 1
    # 목적지에 도달하지 못한 경우
    return -1

N, M = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(N)]
print(bfs())

