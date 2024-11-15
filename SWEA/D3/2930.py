# 2930
# 힙

import heapq

T = int(input())

result = []

for test_case in range(1,T+1):
    n = int(input())
    max_heap = []
    temp = []
    for _ in range(n):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            heapq.heappush(max_heap, (-cmd[1], cmd[1]))
        elif cmd[0] == 2:
            try:
                temp.append(str(heapq.heappop(max_heap)[1]))
            except IndexError:
                temp.append(str(-1))
    result.append("#"+str(test_case)+" "+" ".join(temp))

for j in result:
    print(j)