'''
한 지점씩 놓아보면서
조건을 만족하지 않는다면
백트래킹
전역변수로 결과값을 함수에서 갱신해서
함수 실행 후 갱신된 결과값 출력
'''


import sys
input = sys.stdin.readline

# 퀸을 놓을 수 있는지 확인
def check(row, col):
    # 동일한 열 확인
    for i in range(row):
        if visited[i][col]:
            # 이미 퀸이 존재한다면 False 반환
            return False

    # 왼쪽 대각선
    # 이번에 놓으려는 위치에서 (0,0)까지 이루는 대각선에
    # 이미 퀸이 존재한다면 False 반환
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        # 이미 퀸이 존재하면
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 오른쪽 대각선
    # 이번에 놓으려는 위치에서 (0,N-1)까지 이루는 대각선에
    # 이미 퀸이 존재한다면 False 반환
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    return True


# 백트래킹
def dfs(row):
    global answer
    # 종료 조건
    if row == N:  # 여기까지 왔으면 퀸을 모두 놓았다는 뜻
        answer += 1  # 방법 수 추가
        return

    # 한 행에서 각 열에 놓아보면서 맞는지 확인
    for col in range(N):
        # 여기서 조건을 사용해 퀸을 놓을 수 있는지 없는지 확인
        if check(row, col) is False:
            continue
        visited[row][col] = 1
        # 다음 행으로 넘어가서 확인
        dfs(row + 1)
        # 취소 (초기화)
        visited[row][col] = 0


N = int(input())

visited = [[0] * N for _ in range(N)]  # 방문여부 확인(체스판)
answer = 0  # 퀸을 놓을 수 있는 방법 수

# 0번째 행부터 시작
dfs(0)
print(answer)
