# 11650
# 좌표 정렬하기

n = int(input())
b = [list(map(int, input().split())) for i in range(n)]
b.sort()
for i in range(len(b)):
    print("{0} {1}".format(b[i][0],b[i][1]))