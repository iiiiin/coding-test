# 2817
# 부분 수열의 합

T = int(input())

for test_case in range(1,T+1):
    n,k = map(int, input().split())
    num = list(map(int, input().split()))
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k+1):
            dp[i+1][j] = dp[i][j]
            
            if j >= num[i]:
                dp[i+1][j] += dp[i][j-num[i]]
    result = dp[n][k]
    print(f"#{test_case} {result}")