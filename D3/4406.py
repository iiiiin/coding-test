# 4406
# 모음이 보이지 않는 사람

T = int(input())

for test_case in range(1,T+1):
    vowels = ['a','e','i','o','u']
    s = input()
    result = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
    print(f"#{test_case} {result}")