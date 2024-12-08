# 2110
# 공유기 설치

def solution(target,array,start,end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        point = array[0]
        count = 1
        for i in range(1,len(array)):
            if array[i] - point >= mid:
                count += 1
                point = array[i]
        if count >= target:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

n, c = map(int, input().split())
array = sorted([int(input()) for i in range(n)])
print(solution(c,array,0,array[n-1]-array[0]))