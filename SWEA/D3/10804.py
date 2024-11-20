# 10804
# 문자열의 거울상

T = int(input())

for test_case in range(1,T+1):
    mirror = {'b':'d','d':'b','p':'q','q':'p'}
    s = input()
    result = ""
    for i in range(len(s)):
        result += mirror[s[i]]
    print(f"#{test_case} {result[::-1]}")