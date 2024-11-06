# 17937
# 큰 수의 최대공약수

T = int(input())

for test_case in range(1,T+1):
    a, b = map(int, input().split())
    if a == b:
        result = a
    else:
        result = 1
    print(f"#{test_case} {result}")