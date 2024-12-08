# 1654
# 랜선자르기

n,m = map(int, input().split())
cable = list(sorted([int(input()) for _ in range(n)]))
start = 1
end = cable[-1]
while start <= end:
    mid = (start+end)//2
    total = sum([x//mid for x in cable])
    if total >= m:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)

