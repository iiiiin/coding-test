# 11688
# Calkin-Wilf tree 1

T = int(input())

for test_case in range(1,T+1):
    num, denom = 1, 1
    com = input()
    for s in com:
        if s == "L":
            denom += num
        elif s == "R":
            num += denom
    result = str(num)+" "+str(denom)
    print(f"#{test_case} {result}")