# 3282
# 0/1 Knapsack

T = int(input())

for test_case in range(1,T+1):
    vol, cost = [], []
    n, k = map(int, input().split())
    for _ in range(n):
        v, c = map(int, input().split())
        vol.append(v)
        cost.append(c)
    # dp[i][w]는 처음 i개의 물건들로 무게 w를 채울 때의 최대 가치
    dp = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(k + 1):
            if i == 0 or w == 0:
                # 기저 사례: 물건이 없거나 배낭 용량이 0인 경우
                dp[i][w] = 0
            elif vol[i-1] <= w:
                # 현재 물건을 넣을 수 있는 경우
                # max(현재 물건을 넣는 경우, 현재 물건을 넣지 않는 경우)
                dp[i][w] = max(cost[i-1] + dp[i-1][w-vol[i-1]], dp[i-1][w])
            else:
                # 현재 물건을 넣을 수 없는 경우
                dp[i][w] = dp[i-1][w]
    selected_items = []
    w = k
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= vol[i-1]
    result = sum([cost[x] for x in selected_items])
    print(f"#{test_case} {result}")
