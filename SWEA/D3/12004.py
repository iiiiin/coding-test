# 12004
# 구구단 1

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    for i in range(n,0,-1):
        result = "No"
        if i < 10 and n // i < 10 and n % i ==0:
            result = "Yes"
            break
    print(f"#{test_case} {result}")