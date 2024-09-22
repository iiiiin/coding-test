# 14178
# 1차원 정원

T = int(input())

for test_case in range(1,T+1):
    n, d = map(int, input().split())
    result = n // (2*d+1)
    if n % (2*d+1) >= 1:
        result += 1
    print(f"#{test_case} {result}")