# 7568
# 덩치

n = int(input())
spare = [1]*n
array = [list(map(int, input().split())) for x in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            spare[i] += 1
for i in spare:
    print(i,end=' ')