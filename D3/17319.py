# 17319
# 문자열문자열

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    s = input()
    if n % 2 == 0 and s[:n//2] == s[n//2:]:
        result = "Yes"
    else:
        result = "No"
    print(f"#{test_case} {result}")