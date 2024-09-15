# 1926
# 간단한 369 게임

n = int(input())
result_list = []

for i in range(1,n+1):
    num = str(i)
    clap = ""
    noclap = ""
    cnt = 0
    for j in range(len(num)):
        if num[j] in ["3", "6", "9"]:
            clap += "-"
            cnt = 1
        else:
            noclap += num[j]
    if cnt == 1:
        result_list.append(clap)
    else:
        result_list.append(noclap)
print(*result_list)