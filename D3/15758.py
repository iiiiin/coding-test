# 15758
# 무한 문자열

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

T = int(input())

for test_case in range(1,T+1):
    s, t = input().split()
    k = lcm(len(s),len(t))
    if s*(k//len(s)) == t*(k//len(t)):
        result = "yes" 
    else:
        result = "no"
    print(f"#{test_case} {result}")