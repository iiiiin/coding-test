# 3456
# 직사각형 길이 찾기

T = int(input())

for test_case in range(1,T+1):
    a,b,c = input().split()
    if a == b:
        result = c
    elif a == c:
        result = b
    elif b == c:
        result = a
    print(f"#{test_case} {result}")