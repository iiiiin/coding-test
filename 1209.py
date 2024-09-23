# 1209
# [S/W 문제해결 기본] 2일차 - Sum

# import sys
# sys.stdin = open("input.txt", "r")

for test_case in range(1,11):
    tc = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    hor, ver, diagr, diagl, k = 0, 0, 0, 0, 0
    for i in range(100):
        vertemp = 0
        if hor < sum(arr[i]):
            hor = sum(arr[i])
        for j in range(100):
            vertemp += arr[j][i]
            if i == j:
                diagr += arr[i][j]
            if i + j == 99:
                diagl += arr[i][j]
        if ver < vertemp:
            ver = vertemp
    result = max([hor, ver, diagr, diagl])
    print(f"#{tc} {result}")