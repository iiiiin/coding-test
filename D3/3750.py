# 3750
# Digit sum

T = int(input())

result = []

for test_case in range(1,T+1):
    n = int(input())
    while n >= 10:
        n = sum(list(map(int, list(str(n)))))
    result.append("#"+str(test_case)+" "+str(n))
for x in result:
    print(x)