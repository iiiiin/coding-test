# 16800
# 구구단 걷기

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 2*n
    for i in range(1,int(n**(1/2))+1):
        if n % i == 0 and result > (n//i) + i - 2:
            result = (n//i)+i-2
    print(f"#{test_case} {result}")