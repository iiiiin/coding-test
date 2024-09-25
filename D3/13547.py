# 13547
# 팔씨름

T = int(input())

for test_case in range(1,T+1):
    s = input()
    if 15-len(s) >= 8-s.count("o"):
        result = "YES"
    else:
        result = "NO"
    print(f"#{test_case} {result}")