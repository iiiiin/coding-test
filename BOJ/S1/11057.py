# 11057
# 오르막 수

'''
이전 자리수보다 현재 자리수가 커야 함.
현재 자리수에 따라 이전 자리수의 개수가 정해짐.
각 자리 수가 이전 자리수(작은 부분)에 의해 결정됨.
DP
'''

def asc_num(num):
    dp = [[0] * 10 for _ in range(1000)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[i-1][:j+1])
        if i == num-1:
            return sum(dp[i]) % 10007


N = int(input())

print(asc_num(N))
