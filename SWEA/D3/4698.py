# 4698
# 테네스의 특별한 소수

T = int(input())

for test_case in range(1,T+1):
    d,a,b = map(int, input().split())
    is_prime = [True] * (b+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(b**(1/2)+1)):
        if is_prime[i]:
            for j in range(i*i, b+1, i):
                is_prime[j] = False
    sprime = [x for x in range(a,b+1) if is_prime[x] and str(d) in str(x)]
    result = len(sprime)
    print(f"#{test_case} {result}")