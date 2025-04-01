# 1247
# [S/W 문제해결 응용] 3일차 - 최적 경로

'''
재귀적으로 거리 계산해서 합구하기
가지치기 : min_v보다 크면 return(종료)
동시에 모든 지점으로 이동하는 경우 고려
방문처리 필요
'''

def dfs(cnt, temp, start):
    global min_v
    if temp > min_v:
        return
    if cnt == N:
        to_home = abs(start[0]-home[0])+abs(start[1]-home[1])
        min_v = min(min_v, temp+to_home)
        return

    for i in range(N):
        if not visited[i]:
            to_spot = abs(start[0]-customer[i*2])+abs(start[1]-customer[i*2+1])
            visited[i] = 1
            dfs(cnt+1, temp+to_spot, (customer[i*2],customer[i*2+1]))
            visited[i] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = arr[:2]
    home = arr[2:4]
    customer = arr[4:]
    min_v = float('inf')
    visited = [0] * N
    dfs(0,0, company)
    print(f'#{tc} {min_v}')