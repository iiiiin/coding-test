# 1230
# [S/W 문제해결 기본] 8일차 - 암호문3

for test_case in range(1,11):
    n = int(input())
    pw = list(input().split())
    m = int(input())
    cmd = list(input().split())
    for i in range(len(cmd)):
        if cmd[i] == "I":
            pw[int(cmd[i+1]):int(cmd[i+1])] = cmd[i+3:i+3+int(cmd[i+2])]
        elif cmd[i] == "D":
            pw[int(cmd[i+1]):int(cmd[i+1])+int(cmd[i+2])] = []
        elif cmd[i] == "A":
            pw.extend(cmd[i+2:i+2+int(cmd[i+1])])
    result = pw[:10]
    print(f"#{test_case} ",end="")
    print(*result)