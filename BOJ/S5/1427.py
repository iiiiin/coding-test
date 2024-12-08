# 1427
# 소트 인사이드

n = input()
a = [int(n[x]) for x in range(len(n))]
a = sorted(a, reverse=True)
b = [str(a[x]) for x in range(len(a))]
c = "".join(b)
print(c)