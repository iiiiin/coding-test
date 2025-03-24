# 2669
# 직사각형 네개의 합집합의 면적 구하기

arr = [[0] * 101 for _ in range(101)]

for i in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(b, d):
        arr[j][a:c] = [1] * (c - a)

result = 0

for k in range(len(arr)):
    result += arr[k].count(1)

print(result)