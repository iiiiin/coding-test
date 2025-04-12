# 2527
# 직사각형

'''
성립하는 조건을 먼저 return함
그외에 경우가 각 직사각형의 접하는 경우
1. 한 축으로라도 떨어져 있으면 접할 수 없음
2. 외부의 한 점을 공유하면 한 변을 공유할 수 없음
3. 외부의 한 변을 공유하면 직사각형으로 겹칠 수 없음
'''

import sys
input = sys.stdin.readline

def meet(x1, y1, p1, q1, x2, y2, p2, q2):
    # x, y 축으로 떨어져 있어 분리됨 : d
    if (p1 < x2) or (p2 < x1) or (q1 < y2) or (q2 < y1):
        return "d"
    # 그렇지 않고, 한 점을 공유 : c
    if (p1 == x2 and q1 == y2) or (p1 == x2 and q2 == y1) or (p2 == x1 and q2 == y1) or (p2 == x1 and q1 == y2):
        return "c"
    # 그렇지 않고, 한 변을 공유 : b
    if (q1 == y2) or (q2 == y1) or (p1 == x2) or (p2 == x1):
        return "b"

    return "a"


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(meet(x1, y1, p1, q1, x2, y2, p2, q2))