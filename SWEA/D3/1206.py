# 1206
# [S/W 문제해결 기본] 1일차 - View

for test_case in range(1,11):
    n = int(input())
    heights = list(map(int, input().split()))
    result = 0
    for i in range(2,n-2):
        conditions = [heights[i] > heights[i-2], heights[i] > heights[i-1],
                  heights[i] > heights[i+2], heights[i] > heights[i+1]]
        comp = [heights[i-2],heights[i-1],heights[i+1],heights[i+2]]
        if all(conditions):
            result += heights[i] - max(comp)
    print(f"#{test_case} {result}")