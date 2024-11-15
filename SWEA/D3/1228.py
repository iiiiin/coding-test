# 1228
# [S/W 문제해결 기본] 8일차 - 암호문1

for test_case in range(1,11):
    n = int(input())
    pw_origin = list(map(int, input().split()))
    cmd = int(input())
    cmd_list = list(input().split())
    i = 0
    while i <= len(cmd_list)-1:
        if cmd_list[i] == "I":
            pw_origin[int(cmd_list[i+1]):int(cmd_list[i+1])] = cmd_list[i+3:i+3+int(cmd_list[i+2])]
            i += (3+int(cmd_list[i+2]))
    result = pw_origin[:10]
    print(f"#{test_case} ", end="")
    print(*result)