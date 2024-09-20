# 16910
# 원 안의 점

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 0
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if i**2 + j**2 <= n**2:
                result += 1
    print(f"#{test_case} {result}")