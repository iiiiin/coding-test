# 3142
# 영준이와 신비한 뿔의 숲

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int, input().split())
    twinhorn = n - m
    unicorn = 2*m - n
    print(f"#{test_case} {unicorn} {twinhorn}")


