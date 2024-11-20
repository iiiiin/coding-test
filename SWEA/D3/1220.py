# 1220
# [S/W 문제해결 기본] 5일차 - Magnetic

for test_case in range(1,11):
    t = int(input())
    result = 0
    magnetic = []
    for i in range(100):
        magnetic.append(list(map(int,input().split())))
    magnetic = list(zip(*magnetic))
    for i in range(100):
        flag = 0
        for j in range(100):
            if magnetic[i][j] == 1:
                flag = 1
            elif magnetic[i][j] == 2 and flag == 1:
                result += 1
                flag = 0
    print(f"#{test_case} {result}")