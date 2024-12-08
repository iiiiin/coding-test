# 14501
# 퇴사

n = int(input())
ti, pi = [0]*n, [0]*n
max_pi = [0]*n

for i in range(n):
    ti[i], pi[i] = map(int, input().split())

for i in range(n-1,-1,-1):
    if ti[i] > (n-i):
        if i < n-1:
            max_pi[i] = max_pi[i+1]
    elif i+ti[i] <= (n-1):
        if i == n-1:
            max_pi[i] = pi[i] + max_pi[i+ti[i]]
        else:
            max_pi[i] = max(max_pi[i+1], pi[i] + max_pi[i+ti[i]])
    else:
        if i == n-1:
            max_pi[i] = pi[i]
        else:     
            max_pi[i] = max(max_pi[i+1], pi[i])

print(max(max_pi))