# 16234
# 인구 이동

'''
델타배열로 조건에 맞는지 확인
현재까지 이동한 모든 경로의 인구수를 더하고 경로수로 나눠서 해당 위치의 인구수 구하기
횟수(이동하는 횟수)를 인구 이동 기간으로 반환
BFS로 조건에 맞는 곳을 모두 찾아서 더하기
더한 것으로 계산한 값을 방문리스트로 확인해서 바꾸고
BFS 실행 반복
'''


from collections import deque
import sys

input = sys.stdin.readline

def bfs(si, sj):
    swt = 0
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    temp = []
    sum_temp = 0
    while q:
        r, c = q.popleft()
        sum_temp += ground[r][c]
        temp.append((r,c))
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc]:
                    if L<=abs(ground[r][c] - ground[nr][nc])<=R:
                        q.append((nr,nc))
                        visited[nr][nc] = 1
                        swt = 1
    for i, j in temp:
        ground[i][j] = sum_temp // len(temp)

    return swt


N, L, R = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]

# result = 0
result = 0
# while문
while True:
    # 방문 배열 초기화
    visited = [[0] * N for _ in range(N)]
    # flag 초기화
    flag = 0
    # 2중 for문
    for i in range(N):
        for j in range(N):
            # 방문안했고, 조건을 만족하면 BFS실행
            if not visited[i][j]:
                flag += bfs(i,j)
    # flag 변수가 변하지 않았으면 종료
    if flag == 0:
        break
    # result += 1
    result += 1
print(result)