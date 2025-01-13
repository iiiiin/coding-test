# 22795
# 일곱 부하의 평균

T = int(input())

for test_case in range(1,T+1):
    height = list(map(int, input().split()))
    max_height = max(height)
    result = max(height)
    total = sum(height)
    while True:
        result += 1
        if (total+result) % 7 == 0:
            break
    print(result)