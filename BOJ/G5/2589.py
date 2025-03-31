# 2589
# 보물섬

'''
상하좌우 이동이므로 델타 사용
가장 긴 시간 육지 두 곳을 먼저 찾지 말고
(역발상 역질문)
모든 경우에 대해 BFS로 최단 경로를 찾은 뒤에
그 중 최대 값을 찾자.
=> 시간 초과
=> 말이 조금 다름
=> 최단거리 이동 (BFS),
=> 그 중에 가장 긴 시간이 걸리는 = BFS로 마지막 깊이까지 탐색했을 떄
=> 결론, 어차피 끝(깊이)까지 탐색하는 데, 이게 가장 큰 경우가 보물이 묻혀있는 경우
=> BFS는 최단 경로를 보장하니까
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs(si, sj):
    q = deque()
    visited = [[-1] * M for _ in range(N)]
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            # 조건 1: 인덱스 범위
            if 0<=nr<N and 0<=nc<M:
                # 조건 2: 육지 여부
                if arr[nr][nc] == 'L':
                    # 조건 3: 방문 여부
                    if visited[nr][nc] == -1:
                        q.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + 1
    m = max([max(x) for x in visited])
    return m

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]

# 최댓값
max_v = -1
# 모든 육지 조합에 대해 수행
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            max_v = max(max_v, bfs(i,j))

print(max_v)