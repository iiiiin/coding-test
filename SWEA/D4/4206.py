# 4206
# 연구소 탈출

'''
초마다
1. 바이러스 전파
2. 이동

BFS
처음에 바이러스 위치 모두 큐에 삽입해서
같은 레벨에서 탐색실행
BFS + DFS
먼저 모든 이동가능한 경우를 재귀로 구현

'''

def bfs():

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]