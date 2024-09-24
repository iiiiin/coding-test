# 5948
# 새샘이의 7-3-5 게임

T = int(input())

for test_case in range(1,T+1):
    num = list(map(int, input().split()))
    newnum = set([])
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                newnum.add(num[i]+num[j]+num[k])
    newnum = sorted(list(newnum), reverse=True)
    result = newnum[4]
    print(f"#{test_case} {result}")