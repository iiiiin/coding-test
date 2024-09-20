# 13229
# 일요일

T = int(input())


for test_case in range(1,T+1):
    S = input()
    week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    for i in range(len(week)):
        if S == "SUN":
            result = 7
            break
        elif week[i] == S:
            result = 7 - i - 1
            break
    print(f"#{test_case} {result}")