# 14361
# 숫자가 같은 배수

T = int(input())

for test_case in range(1,T+1):
    n = input()
    mult = 2*int(n)
    result = "impossible"
    while mult <= 10**(len(n))-1:
        flag = 0
        for s in n:
            if n.count(s) != str(mult).count(s):
                flag = 1
                break
        if flag == 1:
            mult += int(n)
        else:
            result = "possible"
            break
    print(f"#{test_case} {result}")