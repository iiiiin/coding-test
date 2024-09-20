# 1215
# [S/W 문제해결 기본] 3일차 - 회문1

for test_case in range(1,11):
    n = int(input())
    arr = []
    result = 0
    for _ in range(8):
        arr.append(input())
    for i in range(8):
        for j in range(8-n+1):
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                result += 1
    t_arr = list(zip(*arr))
    for i in range(8):
        for j in range(8-n+1):
            if t_arr[i][j:j+n] == t_arr[i][j:j+n][::-1]:
                result += 1
    print(f"#{test_case} {result}")
