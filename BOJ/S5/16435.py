# 16435
# 스네이크버드

n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

for i in range(n):
    if l >= h[i]:
        l += 1
    else:
        break
print(l)