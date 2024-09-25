# 3431
# 준환이의 운동관리

T = int(input())

for test_case in range(1,T+1):
    l, u, x = map(int, input().split())
    if x > u:
        result = -1
    elif x <= u and x >= l:
        result = 0
    else:
        result = l - x
    print(f"#{test_case} {result}")