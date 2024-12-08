# 2805
# 나무 자르기

def solution(target,array,start,end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = sum([i - mid if i > mid else 0 for i in array])
        if total >= target:
            start = mid+1
            result = mid
        else:
            end = mid-1
    return result

k, n = map(int, input().split())
array = list(map(int, input().split()))
print(solution(n,array,1,max(array)))