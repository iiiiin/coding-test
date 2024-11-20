# 5356
# 의석이의 세로로 말해요

T = int(input())

for test_case in range(1,T+1):
    s = [input() for _ in range(5)]
    result = ""
    for i in range(max([len(x) for x in s])):
        for j in range(5):
            if i >= len(s[j]):
                continue
            result += s[j][i]
    print(f"#{test_case} {result}")