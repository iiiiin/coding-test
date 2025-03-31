# 6118
# 숨바꼭질

'''
트리 형태로 주어지는 농장의 조감도
BFS로 끝까지 탐색 후,
가장 깊은 탐색 깊이, 동일한 레벨에서의 최솟값 노드 찾기
'''

import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    # 큐 생성
    q = deque()
    # 방문 배열 생성
    visited = [-1] * (N+1)
    # 시작점 처리
    q.append(start)
    visited[start] = 0

    while q:
        v = q.popleft()
        for next_v in adj_list[v]:
            if visited[next_v] == -1:
                q.append(next_v)
                visited[next_v] = visited[v] + 1

    max_v = max(visited)
    max_v_lst = [i for i in range(N+1) if visited[i] == max_v]
    n = max_v_lst[0]
    c = len(max_v_lst)
    return n, max_v, c




# N : 농장(노드) 수
# M : 길(간선) 수
N, M = map(int, input().split())

# 인접 리스트 (1번부터 시작)
adj_list = [[] for _ in range(N+1)]

# 무방향 그래프
for _ in range(M):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    adj_list[B].append(A)

node, dist, cnt = bfs(1)
print(node, dist, cnt)