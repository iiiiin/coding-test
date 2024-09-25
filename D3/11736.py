# 11736
# 평범한 숫자

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    pi = list(map(int, input().split()))
    result = 0
    for i in range(1,n-1):
        conditions = [pi[i], pi[i-1], pi[i+1]]
        if pi[i] != max(conditions) and pi[i] != min(conditions):
            result += 1
    print(f"#{test_case} {result}")