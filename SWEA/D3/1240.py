# 1240
# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    pwcode = []
    rule = {"0001101":0,"0011001":1,"0010011":2,"0111101":3,
            "0100011":4,"0110001":5,"0101111":6,"0111011":7,
            "0110111":8,"0001011":9}
    for i in range(n):
        pwcode.append(list(input()))
    for j in range(n):
        for k in range(m-1,6,-1):
            if pwcode[j][k] == "1":
                extract = pwcode[j][k-55:k+1]
                break
    reextract = []
    for cd in range(0,56,7):
        # injection = int("".join(extract[cd:cd+7]), 2)
        injection = "".join(extract[cd:cd+7])
        reextract.append(rule[injection])
    if (sum([reextract[x] for x in range(8) if x % 2 == 0])*3 + sum([reextract[x] for x in range(8) if x % 2 != 0])) % 10 == 0:
        result = sum(reextract)
    else:
        result = 0
    print(f"#{test_case} {result}")