# 4193
# 수영대회 결승전 (완전 탐색 + 구현)

import sys
sys.stdin = open('sample.txt','r')

from collections import deque

def shortest_time(grid, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]  # 상하좌우 방향 이동
    queue = deque([(start[0], start[1], 0)])  # (x, y, 시간간)
    visited = set()
    visited.add((start[0], start[1], 0))

    while queue:
        x, y, time = queue.popleft()

        # 도착점에 도달한 경우
        if [x, y] == end:
            return time

        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 배열 범위 내에 있고, 방문하지 않았으며, 장애물이 없는 경우
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid):
                continue

            if grid[nx][ny] == 1:
                continue

            if grid[nx][ny] == 2:
                if time % 3 == 2:
                    grid[nx][ny] = 0
                    queue.append((nx, ny, time+1))
                    visited.add((nx, ny, time+1))
                else:
                    continue
            
            if (nx, ny, time+1) not in visited:
                queue.append((nx, ny, time+1))
                visited.add((nx, ny, time+1))

    return -1  # 도달할 수 없는 경우

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))  
    result = shortest_time(arr, start, end)
    print(f"#{test_case} {result}")
