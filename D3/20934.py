# 20934
# 방울 마술

T = int(input())

for test_case in range(1,T+1):
    s, k = input().split()
    s = list(s)
    bell = s.index("o")
    for i in range(int(k)):
        if bell == 0:
            bell += 1
        else:
            bell -= 1
    result = bell
    print(f"#{test_case} {result}")