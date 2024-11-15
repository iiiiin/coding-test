# 10726
# 이진수 표현

T = int(input())

for test_case in range(1,T+1):
    n, m = map(int, input().split())
    if str(bin(m))[-n:] == "1"*n:
        result = "ON"
    else:
        result = "OFF"
    print(f"#{test_case} {result}")