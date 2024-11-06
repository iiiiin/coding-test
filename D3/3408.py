# 3408
# 세가지 합 구하기

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    s1 = n*(1+n)//2
    s2 = n*(1+2*n-1)//2
    s3 = n*(2+2*n)//2
    print(f"#{test_case} {s1} {s2} {s3}")