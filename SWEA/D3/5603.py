# 5603
# [Professional] 건초더미

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 0
    dummy = [int(input()) for _ in range(n)]
    mean_dummy = sum(dummy)/n
    for i in range(n):
        if mean_dummy < dummy[i]:
            result += dummy[i] - mean_dummy
    print(f"#{test_case} {int(result)}")
