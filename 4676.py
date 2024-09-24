# 4676
# 늘어지는 소리 만들기

T = int(input())

for test_case in range(1,T+1):
    s = list(input())
    h = int(input())
    loc = list(map(int, input().split()))
    for i in range(h):
        if loc[i] == 0:
            s[loc[i]] = "-"+s[loc[i]]
        else:
            s[loc[i]-1] = s[loc[i]-1]+"-"
    result = "".join(s)
    print(f"#{test_case} {result}")