# 3085
# 사탕 게임

'''
모든 칸에 대해
완전탐색으로 스왑해보고?
행-열마다 확인해보는 함수로 최대 개수 체크
'''

import sys
input = sys.stdin.readline

def chk():
    # 사탕들
    colors = ['C','P','Z','Y']

    mq = []
    # 각 색상에 대해서
    for c in colors:
        result = []
        # 행, 열 작업 수행
        for i in range(N):
            rv, cv = 0, 0
            for j in range(N):
                if candies[i][j] == c:
                    rv += 1
                elif candies[i][j] != c:
                    result.append(rv)
                    rv = 0
                if candies[j][i] == c:
                    cv += 1
                elif candies[j][i] != c:
                    result.append(cv)
                    cv = 0
            result.append(rv)
            result.append(cv)
        mq.append(max(result))
    return max(mq)

N = int(input())

candies = [list(input()) for _ in range(N)]
delta = [(-1,0),(1,0),(0,-1),(0,1)]
max_v = 0
for i in range(N):
    for j in range(N):
        for dr, dc in delta:
            if 0<=i+dr<N and 0<=j+dc<N:
                if candies[i][j] != candies[i+dr][j+dc]:
                    candies[i][j], candies[i + dr][j + dc] = candies[i + dr][j + dc], candies[i][j]
                    max_v = max(max_v, chk())
                    candies[i][j], candies[i + dr][j + dc] = candies[i + dr][j + dc], candies[i][j]

print(max_v)