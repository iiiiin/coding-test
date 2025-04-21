# 2458
# 키 순서

'''
DFS로 깊이 들어가면서 수행 (재귀)
깊이마다 조건을 만족하는 지 확인
종료조건은 더 이상 없을 때
'''

import sys
input = sys.stdin.readline

def collect_small(num):
    global snum
    if small[num] == []:
        return
    for x in small[num]:
        if not visited[x]:
            visited[x] = 1
            snum.append(x)
            collect_small(x)

def collect_big(num):
    global bnum
    if big[num] == []:
        return
    for x in big[num]:
        if not visited[x]:
            visited[x] = 1
            bnum.append(x)
            collect_big(x)




N, M = map(int, input().split())

# x보다 작은 수를 저장한 리스트
small = [[] for _ in range(N+1)]
# x보다 큰 수를 저장한 리스트
big = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    small[b].append(a)
    big[a].append(b)

answer = 0
for i in range(1,N+1):
    visited = [False] * (N + 1)
    snum = small[i][:]
    bnum = big[i][:]
    collect_small(i)
    visited = [False] * (N + 1)
    collect_big(i)
    snum = list(set(snum))
    bnum = list(set(bnum))
    comp = list(range(1,N+1))
    comp.remove(i)
    if comp == sorted(snum+bnum):
        answer += 1

print(answer)

