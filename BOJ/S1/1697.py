# 1697
# 숨바꼭질

'''
X-1, X+1, 2*X인 노드로 이동하는 경우로
BFS를 수행
이동깊이를 출력(최소보장)
입력과 출력이 같은 경우!
'''

from collections import deque
import sys

input = sys.stdin.readline


def bfs(s):
    if s == end:
        return 1
    q = deque()
    visited = [0] * (100000 + 1)
    q.append(s)
    visited[s] = 1
    while q:
        now = q.popleft()
        for next in [now + 1, now - 1, now * 2]:
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)
                if next == end:
                    return visited[next]


start, end = map(int, input().split())
print(bfs(start) - 1)
