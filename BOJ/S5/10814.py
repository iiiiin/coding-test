# 10814
# 나이순 정렬

n = int(input())
a = [input().split() for i in range(n)]
a = sorted(a, key=lambda x : int(x[0]))
for i in range(len(a)):
    print(f'{a[i][0]} {a[i][1]}')