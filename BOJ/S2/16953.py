# 16953
# A -> B

'''
연산이 모두 숫자가 커지는 방향이므로
더 커지면 확인할 필요가 없음
BFS
A,B의 범위가 10의9제곱, 방문리스트 사용불가?
그런데? 튜플로 해도 리스트 전체를 순회해야 함
그럼 딕셔너리로 저장해서 값을 얻는다?
'''


from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    visited = {}
    q.append((start, 1))
    visited[start] = 1
    while q:
        v, w = q.popleft()
        for x in [int(str(v)+'1'), v*2]:
            if x <= B:
                if visited.get(x):
                    break
                else:
                    q.append((x, w+1))
                    visited[x] = w+1
                if x == B:
                    return w+1

    return -1




A, B = map(int, input().split())
print(bfs(A))