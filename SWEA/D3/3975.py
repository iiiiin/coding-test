# 3975
# 승률 비교하기

T = int(input())

result = []

for test_case in range(1,T+1):
    a,b,c,d = map(int,input().split())
    if a/b == c/d:
        temp = "DRAW"
    elif a/b > c/d:
        temp = "ALICE"
    else:
        temp = "BOB"
    result.append("#"+str(test_case)+" "+temp)

for x in result:
    print(x)