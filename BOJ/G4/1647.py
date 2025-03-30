# 1647
# 도시 분할 계획

import sys
input = sys.stdin.readline

# 루트 찾기 함수
def find_set(x):
    # 자기 자신의 부모라면, 해당 트리의 루트임
    if x == parents[x]:
        return x
    # 아니라면, 재귀함수 실행, 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(a, b):
    # 루트 찾기
    ra = find_set(a)
    rb = find_set(b)
    # 사이클 확인
    if ra == rb:
        return
    # 규칙으로 루트 연결(하나의 루트를 하나의 자식으로)
    if ra < rb:
        parents[rb] = ra
    else:
        parents[ra] = rb

# N : 정점 개수, M : 간선 개수
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
# 간선 오름차순 정렬
edges.sort(key=lambda x : x[2])
# 부모 배열
parents = [i for i in range(N+1)]
# result: 최소 유지비 합
result = 0
# cnt: 간선 개수
cnt = 0
max_v = 0
for s,e,w in edges:
    # 같은 그룹이 아니면
    if find_set(s) == find_set(e):
        continue
    # 두 지점 연결
    union(s,e)
    # 유지비 추가
    result += w
    if max_v < w:
        max_v = w
    # 간선 개수 추가
    cnt += 1
    # N-1개의 간선이 사용되어 연결되어 있으면
    # MST를 구성한 것이므로 종료
    if cnt == N-1:
        break
# 우선 MST를 만들고, 현재 연결 중인 간선 중 가장 가중치가 큰 값을 제거
# 오름차순이니까 마지막을 연결안하고 cnt == N-2에서 끝내면 안되나?
print(result-max_v)

