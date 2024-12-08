# 11057
# 오르막 수

n = int(input())
d = [1]*10

for i in range(1,n):
    result = sum(d)
    x = d[:]
    d[0] = result
    for j in range(1, 10):
        d[j] = d[j-1] - x[j-1]

print(sum(d))