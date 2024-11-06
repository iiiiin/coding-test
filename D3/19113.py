# 19113
# 식료품 가게

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    price = list(map(int, input().split()))
    result = []
    while len(price) > 0:
        for i in range(len(price)):
            if 0.75*price[i] in price:
                temp = 0.75*price[i]
                result.append(price[price.index(temp)])
                price.pop(i)
                price.pop(price.index(temp))
                break
    price.sort()
    print(f"#{test_case}", end=" ")
    print(*result)