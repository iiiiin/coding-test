# 1920
# 수 찾기

def solution(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
array = list(map(int, input().split()))

for i in range(m):
    print(solution(a, array[i], 0, n-1))