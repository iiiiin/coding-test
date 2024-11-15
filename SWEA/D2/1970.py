# 1970
# 쉬운 거스름돈

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    cash_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = []

    for cash in cash_list:
        if n >= cash:
            count.append(n // cash)
            n %= cash
        else:
            count.append(0)
    print("#"+str(test_case+1))
    print(*count)