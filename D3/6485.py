# 6485
# 삼성시의 버스 노선

T = int(input())
result = []

for test_case in range(1,T+1):
    n = int(input())
    bus = [0]*5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a,b+1):
            bus[i] += 1
    p = int(input())
    temp = [bus[int(input())] for x in range(p)]
    result.append(temp)

for j in range(1,T+1):
    print(f"#{j}", end=" ")
    print(*result[j-1])