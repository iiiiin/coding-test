# 12015
# 가장 긴 증가하는 부분 수열 2

def solution(array,target,start,end):
    lb = 0
    while start <= end:
        mid = (start + end) // 2
        if target > array[mid]:
            start = mid + 1
        else:
            lb = mid
            end = mid - 1
    return lb

k = int(input())
array = list(map(int, input().split()))
arr = []
arr.append(array.pop(0))

for i in array:
    if arr[-1] < i:
        arr.append(i)
    else:
        lb = solution(arr,i,0,len(arr)-1)
        arr[lb] = i
print(len(arr))