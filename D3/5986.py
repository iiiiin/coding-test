# 5986
# 새샘이와 세 소수

is_prime = [True]*(1001)
is_prime[0] = is_prime[1] = False

for i in range(2,int(1000**(0.5))+1):
    if is_prime[i]:
        for j in range(i*i, 1001, i):
            is_prime[j] = False

primes = [x for x in range(2,1001) if is_prime[x]]

T = int(input())
for test_case in range(1,T+1):
    result = []
    n = int(input())
    for x in range(len(primes)):
        if primes[x] > n-4:
            break
        for y in range(len(primes)):
            if primes[x]+primes[y] >= n-2:
                break
            for z in range(len(primes)):
                if primes[x]+primes[y]+primes[z] == n:
                    result.append(tuple(sorted([x,y,z])))
                    break
                elif primes[x]+primes[y]+primes[z] > n:
                    break
    result = set(result)
    print(f"#{test_case} {len(result)}")
