# 7576
# 토마토

'''
익은 토마토(1)인 지점을 모두 큐에 넣고
BFS를 수행 => 그래야 동시에 곳곳의 토마토가 상하좌우로 익는 효과 발생
이러한 BFS를 수행 후 0이 남아 있으면 -1
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    while q:
        r, c, t = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<M:
                if tomatos[nr][nc] == 0:
                    tomatos[nr][nc] = 1
                    q.append((nr,nc,t+1))

    # BFS 수행 후에도 익지 않은 토마토(0)가 있으면 -1 반환
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                return -1

    # 그렇지 않으면 모든 토마토가 익는데까지 걸린 시간 반환
    return t

M, N = map(int, input().split())

delta = [(-1,0),(1,0),(0,-1),(0,1)]

tomatos = [list(map(int, input().split())) for _ in range(N)]


q = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            q.append((i,j,0))


print(bfs())


