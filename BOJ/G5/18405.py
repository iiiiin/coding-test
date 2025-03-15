# 18405
# 경쟁적 전염

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    for x,y,_ in virus:
        q.append((x,y,0))
    while q:
        r, c, t = q.popleft()
        if t == S:
            return
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<N and not arr[nr][nc]:
                q.append((nr,nc, t+1))
                arr[nr][nc] = arr[r][c]


delta = [(-1,0),(1,0),(0,-1),(0,1)]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            virus.append((i,j,arr[i][j]))
virus.sort(key=lambda x:x[2])
cnt = 0
bfs()
print(arr[X-1][Y-1])
