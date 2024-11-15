# 13428
# 숫자 조작

T = int(input())

for test_case in range(1,T+1):
    n = list(input())
    minval = maxval = int("".join(n))
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            temp = n[:]
            temp[i], temp[j] = temp[j], temp[i]
            if temp[0] == "0":
                continue
            minval = min(minval, int("".join(temp)))
            maxval = max(maxval, int("".join(temp)))

    print(f"#{test_case} {minval} {maxval}")