# 3307
# 최장 증가 부분 수열

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1]*n
    for i in range(n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    result = max(dp)
    print(f"#{test_case} {result}")