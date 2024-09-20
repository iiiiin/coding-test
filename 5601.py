# 5601
# [Professional] 쥬스 나누기

T = int(input())

for test_case in range(1,T+1):
    juice = int(input())
    result = ["1"+"/"+str(juice) for _ in range(juice)]
    print(f"#{test_case} ", end="")
    print(*result)