# 5549
# 홀수일까 짝수일까

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    if n % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    print(f"#{test_case} {result}")