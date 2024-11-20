# 10570
# 제곱 팰린드롬 수

T = int(input())

for test_case in range(1,T+1):
    a, b = map(int, input().split())
    result = 0
    for i in range(a,b+1):
        if str(i) == str(i)[::-1] and "{:g}".format(i**(1/2)) == ("{:g}".format(i**(1/2)))[::-1]:
            result += 1
    print(f"#{test_case} {result}")