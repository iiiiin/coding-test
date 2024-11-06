# 5688
# 세제곱근을 찾아라

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 0
    i = 0
    while i**3 <= n:
        if i ** 3 == n:
            result = i
            break
        i += 1
    if result == 0:
        result = -1
    print(f"#{test_case} {result}")