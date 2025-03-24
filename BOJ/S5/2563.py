# 2563

a = [[0]*100 for i in range(100)]
n = int(input())
for i in range(n):
    b, c = map(int, input().split())
    for j in range(10):
        for k in range(10):
            a[99-c+1-j][b-1+k] += 1

t = 0
for s in range(len(a)):
    for r in range(len(a)):
        if a[s][r] != 0:
            t += 1
print(t)
