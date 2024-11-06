# 3131
# 100만 이하의 모든 소수

is_prime = [True] * (10**6 + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int((10**6)**(1/2))+1):
    if is_prime[i]:
        for j in range(i*i, 10**6+1, i):
            is_prime[j] = False

primes = [x for x in range(2, 10**6+1) if is_prime[x]]
print(*primes)
