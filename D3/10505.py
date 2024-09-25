# 10505
# 소득 불균형

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    income = list(map(int, input().split()))
    result = len([income[x] for x in range(n) if income[x] <= sum(income)/n])
    print(f"#{test_case} {result}")