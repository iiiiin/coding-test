# 1289
# 원재의 메모리 복구

T = int(input())

for test_case in range(1,T+1):
    s = input()
    bit = "0"
    result = 0
    for i in range(len(s)):
        if s[i] != bit:
            if s[i] == "1":
                bit = "1"
            else:
                bit = "0"
            result += 1
    print(f"#{test_case} {result}")