# 3190
# 뱀

'''
구현
델타탐색으로 방향을 전환하고
이동하는 데 해당 지점이 벽이나 현재 자신의 몸이면 종료
뱀의 몸이 위치한 곳을 모두 덱에 삽입
1. 이동한 곳이 벽이거나, 덱에 동일한 인덱스가 있다면 종료
2. 그게 아니고, 사과가 있다면 사과만 없애서 처리 => 이동한 인덱스 추가
3. 사과가 없다면, FIFO로 dequeue실행 => 이동한 인덱스 추가
시간마다 방향 전환 확인하여 방향 전환 후 이동
'''

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    # 사과 놓기
    arr[r - 1][c - 1] = 1
L = int(input())
change = [input().split() for _ in range(L)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 초기방향 오른쪽
d = 1
# 초기시작 위치
q = deque()
q.append((0, 0))
t = 0
while True:
    # 현재 시간에 방향 확인
    for x, c in change:
        # 현재 시간이면 방향 바꾸기
        if t == int(x):
            if c == 'D':
                d = (d + 1) % 4
            elif c == 'L':
                d = (d + 3) % 4
            break
    # 이동 시간 증가
    t += 1
    # 몸길이 늘려 머리를 다음칸에 위치
    nr, nc = q[-1][0] + delta[d][0], q[-1][1] + delta[d][1]
    # 벽 또는 자기자신을 만났을 때
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        break
    elif (nr, nc) in q:
        break
    else:
        # 사과가 있다면
        if arr[nr][nc] == 1:
            # 사과 처리
            arr[nr][nc] = 0
            q.append((nr, nc))
        # 사과가 없다면
        else:
            q.popleft()
            q.append((nr, nc))

print(t)
