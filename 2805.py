# 2805
# 농작물 수확하기

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    mid = n // 2
    k = 0
    flag = 0
    result = 0
    for i in range(n):
        farm = list(map(int, list(input())))
        if k == 0:
            result += farm[mid]
        else: 
            result += sum(farm[mid-k:mid+k+1])
        if flag == 0:
            k += 1
        else:
            k -= 1
        if k == mid:
            flag = 1
    print(f"#{test_case} {result}")