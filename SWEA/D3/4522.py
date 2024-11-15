# 4522
# 세상의 모든 팰린드롬

T = int(input())

for test_case in range(1,T+1):
    s = input()
    s_rev = s[::-1]
    result = "Exist"
    for i in range(len(s)):
        if s[i] == s_rev[i] or s[i] == "?" or s_rev[i] == "?":
            continue
        else:
            result = "Not exist"
            break
    print(f"#{test_case} {result}")