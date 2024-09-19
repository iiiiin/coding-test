# 1976
# 시각 덧셈

T = int(input())

for test_case in range(1,T+1):
    ha, ma, hb, mb = map(int, input().split())
    hour = (ha + hb) % 12 + (ma + mb) // 60
    minute = (ma + mb) % 60
    print(f"#{test_case} {hour} {minute}")