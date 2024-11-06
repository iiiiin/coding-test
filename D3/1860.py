# 1860
# 진기의 최고급 붕어빵

T = int(input())

for test_case in range(1,T+1):
    n,m,k = map(int, input().split())
    customer = list(sorted(list(map(int, input().split()))))
    result = "Possible"
    timing = m
    flag = 0
    for i in range(0,len(customer),k):
        for x in customer[i:i+k]:
            if x < timing:
                result = "Impossible"
                flag = 1
                break
        if flag == 1:
            break
        else:
            timing += m
    print(f"#{test_case} {result}")