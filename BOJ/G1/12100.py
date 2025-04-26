# 12100
# 2048 (Easy)

'''
재귀를 5회
각 깊이마다 상하좌우로 뻗어나감
1. 한 쪽으로 이동시키기
2. 동일한 2개를 더해서 하나로 만들기
'''

import sys
input = sys.stdin.readline

def dfs(cnt, array):
    global max_v
    # 종료조건
    if cnt == 5:
        val = 0
        # 가장 큰 블록 찾기
        for i in range(N):
            for j in range(N):
                val = max(val, int(array[i][j]))
        max_v = max(max_v, val)
        return
    # 현재 깊이의 배열 복사
    temp = [row[:] for row in array]
    # 좌측
    for i in range(N):
        t_v = [x for x in temp[i] if x != '0']
        v_v = []
        idx = 0
        while idx < len(t_v):
            if idx + 1 < len(t_v) and t_v[idx] == t_v[idx + 1]:
                v_v.append(str(int(t_v[idx]) * 2))
                idx += 2
            else:
                v_v.append(t_v[idx])
                idx += 1
        outro = v_v + ['0'] * (N - len(v_v))
        temp[i] = [x for x in outro if x]
    dfs(cnt+1, temp)
    temp = [row[:] for row in array]
    # 우측
    for i in range(N):
        t_v = [x for x in temp[i] if x != '0'][::-1]
        v_v = []
        idx = 0
        while idx < len(t_v):
            if idx + 1 < len(t_v) and t_v[idx] == t_v[idx + 1]:
                v_v.append(str(int(t_v[idx]) * 2))
                idx += 2
            else:
                v_v.append(t_v[idx])
                idx += 1
        outro = ['0'] * (N - len(v_v)) + v_v[::-1]
        temp[i] = [x for x in outro if x]
    dfs(cnt+1, temp)
    # 상측 (전치 후 좌측 후 전치)
    temp = [row[:] for row in array]
    temp = list(map(list, zip(*temp)))
    for i in range(N):
        t_v = [x for x in temp[i] if x != '0']
        v_v = []
        idx = 0
        while idx < len(t_v):
            if idx + 1 < len(t_v) and t_v[idx] == t_v[idx + 1]:
                v_v.append(str(int(t_v[idx]) * 2))
                idx += 2
            else:
                v_v.append(t_v[idx])
                idx += 1
        outro = v_v + ['0'] * (N - len(v_v))
        temp[i] = [x for x in outro if x]
    temp = list(map(list, zip(*temp)))
    dfs(cnt + 1, temp)
    # 하측 (전치 후 우측 후 전치)
    temp = [row[:] for row in array]
    temp = list(map(list, zip(*temp)))
    for i in range(N):
        t_v = [x for x in temp[i] if x != '0'][::-1]
        v_v = []
        idx = 0
        while idx < len(t_v):
            if idx + 1 < len(t_v) and t_v[idx] == t_v[idx + 1]:
                v_v.append(str(int(t_v[idx]) * 2))
                idx += 2
            else:
                v_v.append(t_v[idx])
                idx += 1
        temp[i] = ['0'] * (N - len(v_v)) + v_v[::-1]
        temp[i] = [x for x in temp[i] if x]
    temp = list(map(list, zip(*temp)))
    dfs(cnt + 1, temp)

N = int(input())

arr = [input().split() for _ in range(N)]
max_v = 0
dfs(0, arr)
print(max_v)
