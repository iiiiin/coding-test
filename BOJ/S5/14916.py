# 14916
# 거스름돈

n = int(input())
result = -1

for i in range(n // 5,-1,-1):
    if (n - (5*i)) % 2 == 0:
        result = i + ((n - (5*i)) // 2)
        break
    
print(result)