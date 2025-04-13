# 22683
# 나무 베기

'''
BFS를 하되, 방문 배열에 방문 횟수가 아닌 최소 조작 횟수를 저장
모든 탐색을 수행하고, Y 위치에 저장된 visited값을 출력
현재 위치에서 전진, 우회전, 좌회전을 할 수 있음
'''

from collections import deque


def find_point(s):
    for i in range(N):
        for j in range(N):
            if fields[i][j] == s:
                return i, j


def bfs(si, sj, k, d, cnt):
    q = deque([(si, sj, k, d, cnt)])
    # 최소 조작 횟수 기록 리스트 생성
    visited = [[[[float('inf')] * 4 for _ in range(k + 1)] for _ in range(N)] for _ in range(N)]
    # 최소 조작 횟수 기록
    # si,sj 위치, 방향 d에서 k만큼 베기 횟수가 남은 상황의 최소조작횟수 cnt
    visited[si][sj][k][d] = cnt
    while q:
        cr, cc, ck, cd, ccnt = q.popleft()
        # 전진
        nr = cr + delta[cd][0]
        nc = cc + delta[cd][1]
        # 인덱스 접근 가능하면
        if 0 <= nr < N and 0 <= nc < N:
            # 조작횟수 증가
            ncnt = ccnt + 1
            # 베기 필요없는 곳이라면
            if fields[nr][nc] != 'T':
                # 다음 이동한 지점에서, 현재 베기 횟수와 방향인 경우의 저장된 조작횟수 비교
                # 현재 계산한 값이 더 작다면 갱신
                if visited[nr][nc][ck][cd] > ncnt:
                    visited[nr][nc][ck][cd] = ncnt
                    q.append((nr, nc, ck, cd, ncnt))
            # 나무인 곳이라면
            else:
                # 베기 횟수가 남았을 경우
                if ck > 0:
                    # 동일하게, 다음 지점에서, 현재 베고 남은 횟수와 방향인 경우의 저장된 조작횟수 비교
                    # 무조건 베어야 이동가능하므로, ck-1
                    if visited[nr][nc][ck - 1][cd] > ncnt:
                        visited[nr][nc][ck - 1][cd] = ncnt
                        q.append((nr, nc, ck - 1, cd, ncnt))

        # 좌회전
        nd = (cd + 3) % 4
        ncnt = ccnt + 1
        # 다시 조건을 확인하여 현재 상황(방향이 달라짐)의 조작횟수 비교 후 갱신
        if visited[cr][cc][ck][nd] > ncnt:
            visited[cr][cc][ck][nd] = ncnt
            q.append((cr, cc, ck, nd, ncnt))

        # 우회전
        nd = (cd + 1) % 4
        ncnt = ccnt + 1
        # 다시 조건을 확인하여 현재 상황(방향이 달라짐)의 조작횟수 비교 후 갱신
        if visited[cr][cc][ck][nd] > ncnt:
            visited[cr][cc][ck][nd] = ncnt
            q.append((cr, cc, ck, nd, ncnt))

    # 도착점 위치의 배열에서 최솟값 찾기
    min_v = float('inf')
    for i in range(k + 1):
        for j in range(4):
            min_v = min(min_v, visited[ei][ej][i][j])

    # 바뀌지 않았으면 찾지 못한 것
    if min_v == float('inf'):
        return -1
    else:
        return min_v


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    fields = [input() for _ in range(N)]
    # 현재 위치 X 찾기
    si, sj = find_point('X')
    ei, ej = find_point('Y')

    print(f'#{tc} {bfs(si, sj, K, 0, 0)}')
