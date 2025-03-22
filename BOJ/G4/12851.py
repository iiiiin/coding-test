# 12851
# 숨바꼭질 2

'''
BFS를 수행하면서
동생 위치에 도착하면 시간 저장(최소 시간)
'''

from collections import deque

def bfs(s):
    ways = [0] * (100000+1)
    q = deque()
    q.append(s)
    t, cnt = 0, 0
    while q:
        now = q.popleft()
        val = ways[now]
        if now == K:
            t = val
            cnt += 1
            continue

        temp = [now-1,now+1,now*2]
        for x in temp:
            if 0<= x <= 100000:
                if ways[x] == 0 or ways[x] == ways[now] + 1:
                    ways[x] = ways[now] + 1
                    q.append(x)

    return t, cnt

N, K = map(int, input().split())
min_t, cases = bfs(N)
print(min_t, cases, sep='\n')