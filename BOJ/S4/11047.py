# 11047
# 동전 0

n, m = map(int, input().split())
array = [int(input()) for x in range(n)]
count = 0
for i in array[::-1]:
    if i <= m and m // i > 0:
        count += m // i
        m = m % i
print(count)