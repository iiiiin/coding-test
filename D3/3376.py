# 3376
# 파도반 수열

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    seq = [1,1,1,2,2]
    if n > 5:
        i = 5
        while i <= n:
            seq.append(seq[i-1]+seq[i-5])
            i += 1
    result = seq[n-1]
    print(f"#{test_case} {result}")


# 1 1 1 (1+1) (1+1) (1+(1+1)) (1+(1+(1+1))) 
# (1+(1+(1+(1+1)))) ((1+1)+(1+(1+(1+(1+1))))) 
# ((1+(1+1))+((1+1)+(1+(1+(1+(1+1))))))