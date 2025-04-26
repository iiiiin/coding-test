# 15683
# 감시

'''
DFS
최소 사각지대 수 갱신
'''

import sys

input = sys.stdin.readline

delta = [(-1,0),(0,1),(1,0),(0,-1)]
directions = [[],
              # 1번 한 방향씩
              [[0],[1],[2],[3]],
              # 2번 상하, 좌우
              [[0,2],[1,3]],
              # 3번 4가지 방향
              [[0,1],[1,2],[2,3],[3,0]],
              # 4번 4가지 방향
              [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
              # 5번 1가지 방향
              [[0,1,2,3]]
              ]

def dfs(idx, array):
    global min_v
    if idx == len(cctvs):
        # 사각지대 찾기
        val = 0
        for i in range(N):
            for j in range(M):
                if array[i][j] == 0:
                    val += 1
        min_v = min(min_v, val)
        return

    r,c = cctvs[idx][0], cctvs[idx][1]
    for d in directions[array[r][c]]:
        temp = [row[:] for row in array]
        for u in d:
            k = 1
            while True:
                nr, nc = r+k*delta[u][0], c+k*delta[u][1]
                if not 0<=nr<N or not 0<=nc<M or temp[nr][nc] == 6:
                    break
                elif temp[nr][nc] == 0:
                    temp[nr][nc] = 7
                k += 1
        dfs(idx+1, temp)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
for i in range(N):
    for j in range(M):
        if 0<arr[i][j]<6:
            cctvs.append((i,j))
min_v = float('inf')
visited = [[0] * M for _ in range(N)]
dfs(0, arr)
print(min_v)

