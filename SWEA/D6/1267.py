# 1267
# [S/W 문제해결 응용] 10일차 - 작업순서

'''
BFS로 순차처리
역순으로 추가하면 어떨까?
'''
from collections import deque

def bfs():
    q = deque()
    visited = [0] * (V + 1)
    # 다음 작업이 없는 정점 큐에 추가
    for x in range(1, V + 1):
        if not graph[x]:
            q.append(x)

    while q:
        now = q.popleft()
        if not visited[now]:
            answer.append(now)
            visited[now] = 1
        for v in range(1,V+1):
            if not visited[v] and now in graph[v]:
                q.append(v)
                visited[v] = 1
                answer.append(v)


for tc in range(1,11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        graph[edges[i*2]].append(edges[i*2+1])

    answer = []
    bfs()

    print(f'#{tc}', *answer[::-1])

