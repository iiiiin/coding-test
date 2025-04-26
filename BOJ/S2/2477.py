# 2477
# 참외밭

'''
4가지 경우 (육각형, 반시계방향이므로, 5개 점을 확인하면 나머지 한 개 점의 위치 고정)
계산
'''

import sys
input = sys.stdin.readline

# 동: 1, 서: 2, 남: 3, 북: 4
shapes = [[3,1,3,1],[4,2,4,2],[1,4,1,4],[2,3,2,3]]

def find_area():
    for s in shapes:
        for i in range(len(stack)-3):
            temp = ds[i:i + 4]
            if temp == s:
                vs = [x[1] for x in stack if x[0] not in set(temp)]
                result = K * (vs[0]*vs[1] - stack[i+1][1]*stack[i+2][1])
                return result

K = int(input())
stack = []
for _ in range(6):
    d, l = map(int, input().split())
    stack.append((d,l))
# 어느 지점에서 시작할 지 모르니 패턴을 찾을 수 있도록 2배로 연장
stack += stack

ds = [x[0] for x in stack]

print(find_area())
