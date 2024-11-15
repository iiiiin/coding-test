# 6019
# 기차 사이의 파리

T = int(input())

for test_case in range(1,T+1):
    d, a, b, f = map(float, input().split())
    result = f * (d / (a+b))
    print(f"#{test_case} {result}")