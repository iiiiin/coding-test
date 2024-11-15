# 20551
# 증가하는 사탕 수열

T = int(input())

for test_case in range(1,T+1):
    a,b,c = map(int, input().split())
    result = 0
    while True:
        if a < 1 or b <= 1 or c <= 1:
            result = -1
            break
        if a >= b:
            a -= 1
            result += 1
        if b >= c:
            b -= 1
            result += 1
        if a < b and b < c:
            break
    print(f"#{test_case} {result}")