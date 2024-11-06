# 3032
# 홍준이의 숫자 놀이

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

T = int(input())


for test_case in range(1,T+1):
    a,b = map(int, input().split())
    gcd, x, y = extended_gcd(a, b)
    print(f"#{test_case} {x} {y}")