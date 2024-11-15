# 12221
# 구구단2

T = int(input())

for test_case in range(1,T+1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        result = -1
    else:
        result = a*b
    print(f"#{test_case} {result}")