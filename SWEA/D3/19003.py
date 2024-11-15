# 19003
# 팰린드롬 문제

T = int(input())

for test_case in range(1,T+1):
    result = 0
    flag = 0
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][::-1] == s[j] and i != j:
                result += 2*m
                s[i] = ""
            elif s[i] == s[i][::-1] and flag == 0 and s[i] != "":
                result += m
                flag = 1
    print(f"#{test_case} {result}")