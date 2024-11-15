# 4371
# 항구에 들어오는 배

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    goodday = [int(input()) for _ in range(n)]
    cycle = [0]
    for i in range(1,n):
        flag = 0
        for j in range(1,len(cycle)):
            if (goodday[i]-goodday[0]) % cycle[j] == 0:
                flag = 1
                break
        if flag == 0:
            cycle.append(goodday[i]-goodday[0])
    print(f"#{test_case} {len(cycle)-1}")
