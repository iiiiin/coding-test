# 1300
# K번째 수

n = int(input())
k = int(input())
start, end = 1, k
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in range(1, n+1):
        result += min(mid//i, n)
    if result >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)