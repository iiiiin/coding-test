# 2960
# 에라토스테네스의 체

n, k = map(int, input().split())
cnt = 0
flag = 0

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False


for i in range(2, n+1):
    for j in range(i, n+1, i):
        if is_prime[j]:
            is_prime[j] = False
            cnt += 1
        if cnt == k:
            result = j
            flag = 1
            break
    if flag == 1:
        break
print(j)