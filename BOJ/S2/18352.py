# 18352
# 특정 거리의 도시 찾기

from collections import deque

import sys
input = sys.stdin.readline

def bfs(node):
    visited = [-1]*(N+1)
    q = deque()
    q.append(node)
    visited[node] = 0
    flag = 0
    while q:
        now = q.popleft()
        for new in adj_list[now]:
            if visited[new] == -1:
                q.append(new)
                visited[new] = visited[now] + 1
                if visited[new] > K:
                    flag = 1
                    break
            if flag:
                break

    result = sorted([x for x in range(N+1) if visited[x] == K])
    return result


N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
temp = bfs(X)
if temp:
    print(*temp, sep='\n')
else:
    print(-1)