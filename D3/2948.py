# 2948
# 문자열 교집합

T = int(input())

for test_case in range(1,T+1):
    n,m = map(int, input().split())
    s1 = list(input().split())
    s2 = list(input().split())
    result = n+m-len(set(s1 + s2))
    print(f"#{test_case} {result}")