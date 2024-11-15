# 10912
# 외로운 문자

T = int(input())

for test_case in range(1,T+1):
    s = list(input())
    result = ""
    s_dict = dict(sorted({x:0 for x in set(s)}.items()))
    for i in range(len(s)):
        s_dict[s[i]] += 1
    for j in s_dict.keys():
        if s_dict[j] % 2 != 0:
            result += j
    if result == "":
        result = "Good"
    print(f"#{test_case} {result}")