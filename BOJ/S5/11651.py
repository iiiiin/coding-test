# 11651
# 좌표 정렬하기 2

n = int(input())
b =  [tuple(map(int, input().split())) for x in range(n)]
b.sort(key=lambda x : (x[1],x[0]))
for i in range(len(b)):
    print(f'{b[i][0]} {b[i][1]}')