# 1225
# S/W 문제해결 기본] 7일차 - 암호생성기

for test_case in range(1,11):
    t = int(input())
    pw = list(map(int, input().split()))
    i = 1
    while pw[-1] > 0:
        if pw[0]-i > 0:
            val = pw[0]-i
        else:
            val = 0
        pw.append(val)
        pw.pop(0)
        i += 1
        if i > 5:
            i = 1
    print(f"#{t} ",end="")
    print(*pw)