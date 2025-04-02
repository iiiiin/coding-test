# 1258
# [S/W 문제해결 응용] 7일차 - 행렬찾기

'''
완전탐색
DP 방법 찾아보기
'''

# 0이 아닌 부분의 행과 열 찾는 함수
def bruteforce(si, sj):
    x, y = 0, 0
    # 인덱스 범위를 넘어가지 않도록 조건 설정, 0이 아닌 부분일 때만 수행
    while si+x < N and sj+y < N and arr[si + x][sj + y] != 0:
        # 2중 반복으로 먼저 열 순회(0이 나오기 전까지 열 이동)
        while si+x < N and sj+y < N and arr[si + x][sj + y] != 0:
            visited[si + x][sj + y] = 1
            y += 1
        res_y = y
        y = 0
        # 다시 행 이동하여 행 순회
        x += 1
    # 행과 열 반환
    return [x, res_y]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 배열
    visited = [[0] * N for _ in range(N)]
    result = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 방문처리 되지 않고, 0이 아닌 지점에서 완전탐색 수행
            if arr[i][j] != 0 and visited[i][j] == 0:
                result.append(bruteforce(i, j))
                cnt += 1
    print(f'#{tc}', cnt, end=' ')
    # 조건: 크기가 같을 경우, 행 오름차순 정렬
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    for i in range(len(result)):
        if i == len(result) - 1:
            print(*result[i])
        else:
            print(*result[i],end=' ')
