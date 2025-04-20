# 17290
# Crazy_aRcade_Good

'''
상하좌우 델타 탐색으로 배열 이동하는 모든 경우 고려
BFS
안전 범위에 도달하면 반환
폭탕의 행과 열을 리스트에 저장
조건 : 현재 행, 열이 리스트에 있지 않은 경우 종료
'''

from collections import deque

import sys
input = sys.stdin.readline

def bfs(si, sj):
    if si not in avoid_x and sj not in avoid_y:
        return 0
    q = deque([(si,sj)])
    visited = [[-1] * 10 for _ in range(10)]
    visited[si][sj] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr,c+dc
            if 0<=nr<10 and 0<=nc<10:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    if nr not in avoid_x and nc not in avoid_y:
                        return visited[nr][nc]
                    q.append((nr,nc))


sr, sc = map(int, input().split())
arr = [input() for _ in range(10)]
avoid_x, avoid_y = set(), set()
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'o':
            avoid_x.add(i)
            avoid_y.add(j)
print(bfs(sr-1,sc-1))