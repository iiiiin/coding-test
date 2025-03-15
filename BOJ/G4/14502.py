# 14502
# 연구소

'''
완전탐색: 0인 곳 중 3 지점 조합
바이러스: BFS 전파
안전영역: 0 세기
'''

from collections import deque
import sys

input = sys.stdin.readline

def dfs_empty(idx, cnt, temp):
    global empty_comb
    if cnt > 3:
        return
    if idx == len(empty):
        if cnt == 3:
            empty_comb.append(temp)
        return
    dfs_empty(idx+1, cnt+1, temp+[empty[idx]])
    dfs_empty(idx+1, cnt, temp)

def bfs_virus(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<M and not copied_map[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                copied_map[nr][nc] = 2



N, M = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1,0),(1,0),(0,-1),(0,1)]

empty = []
for i in range(N):
    for j in range(M):
        if not virus_map[i][j]:
            empty.append((i,j))

empty_comb = []
dfs_empty(0, 0, [])

result = 0
for x in empty_comb:
    copied_map = [x[:] for x in virus_map]
    visited = [[0] * M for _ in range(N)]
    copied_map[x[0][0]][x[0][1]] = 1
    copied_map[x[1][0]][x[1][1]] = 1
    copied_map[x[2][0]][x[2][1]] = 1
    for i in range(N):
        for j in range(M):
            if copied_map[i][j] == 2 and not visited[i][j]:
                bfs_virus(i, j)
    max_v = 0
    for i in range(N):
        for j in range(M):
            if copied_map[i][j] == 0:
                max_v += 1
    result = max(result, max_v)


print(result)