# 9205
# 맥주 마시면서 걸어가기

def dfs(r, c):
    global result
    if result == 'happy':
        return
    if abs(fr-r)+abs(fc-c) <= 1000:
        result = 'happy'
        return
    for idx, x in enumerate(convenience):
        if not visited[idx] and abs(x[0]-r) + abs(x[1]-c) <= 1000:
            visited[idx] = 1
            dfs(x[0], x[1])
            # visited[idx] = 0
            # 백트래킹 필요없음

t = int(input())

for _ in range(t):
    n = int(input())
    hr, hc = map(int, input().split())
    convenience = [list(map(int, input().split())) for _ in range(n)]
    fr, fc = map(int, input().split())
    visited = [0] * n
    result = 'sad'
    dfs(hr,hc)
    print(result)
