# 12741
# 두 전구

T = int(input())
answer = []

for test_case in range(1,T+1):
    a,b,c,d = map(int, input().split())
    result = min(b,d) - max(a,c)
    if result < 0:
        answer.append("#"+str(test_case)+" "+"0")
    else:
        answer.append("#"+str(test_case)+" "+str(result))
for x in answer:
    print(x)