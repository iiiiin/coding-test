# 6692
# 다솔이의 월급 상자

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 0
    for i in range(n):
        a, b = map(float, input().split())
        result += a*b
    print(f"#{test_case} {result}")