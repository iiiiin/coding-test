# 5431
# 민석이의 과제 체크하기

T = int(input())

for test_case in range(1,T+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))
    result = [x for x in range(1, n+1) if x not in submit]
    print(f"#{test_case} ", end="")
    print(*result)