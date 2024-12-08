# 2108
# 통계학

n = int(input())
count_list = [0]*8001
ans = dict()
array = []

for i in range(n):
    k = int(input())
    count_list[k] += 1

for i in range(8001):
    if count_list[i] > 0 and i <= 4000:
        ans[i] = count_list[i]
    elif count_list[i] > 0 and i > 4000:
        ans[i-8001] = count_list[i-8001]
ans = dict(sorted(ans.items()))
mv = max(ans.values())
a = [x for x in ans.keys() if ans[x] == mv]
for i in ans.keys():
    array += [i]*ans[i]
if len(a) > 1:
    d = a[1]
else:
    d = a[0]

print(round(sum(array)/n))
print(array[len(array)//2])
print(d)
print(abs(array[-1]-array[0]))