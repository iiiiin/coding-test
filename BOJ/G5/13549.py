# 13549
# 숨바꼭질 3

'''
BFS
순간이동 고려
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    if start == E:
        return 0
    visited = [-1] * (100000 + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        now = q.popleft()
        for nxt in [now*2, now-1, now+1]:
            if 0<=nxt<=100000 and visited[nxt] == -1:
                q.append(nxt)
                if nxt == now*2:
                    visited[nxt] = visited[now]
                else:
                    visited[nxt] = visited[now] + 1
                if nxt == E:
                    return visited[nxt]

S, E = map(int, input().split())
print(bfs(S))