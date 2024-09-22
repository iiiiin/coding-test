# 10200
# 구독자 전쟁

T = int(input())

for test_case in range(1,T+1):
    n, a, b = map(int, input().split())
    result = []
    result.append(min(a,b))
    if n >= a+b:
        result.append(0)
    else:
        result.append(a+b-n)
    print(f"#{test_case} {result[0]} {result[1]}")
