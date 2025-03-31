# 1012
# 유기농 배추

'''
배열 돌면서 BFS 실행 횟수?
방문처리 필요없이 그냥 1 -> 0으로 처리
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs(si, sj):
    q = deque()
    q.append((si,sj))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<M:
                if cabbage[nr][nc] == 1:
                    q.append((nr,nc))
                    cabbage[nr][nc] = 0



T = int(input())

delta = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        cabbage[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)