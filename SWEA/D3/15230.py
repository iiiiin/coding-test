# 15230
# 알파벳 공부

T = int(input())

for test_case in range(1,T+1):
    s = "abcdefghijklmnopqrstuvwxyz"
    comp = input()
    result = 0
    for i in range(len(comp)):
        if comp[i] == s[i]:
            result += 1
        else:
            break
    print(f"#{test_case} {result}")
