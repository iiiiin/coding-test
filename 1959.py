# 1959
# 두 개의 숫자열

T = int(input())
for test_case in range(1,T+1):
    result = - 11
    n, m = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    if len(aj) == len(bj):
        result = sum([aj[i]*bj[i] for i in range(len(aj))])
    elif len(aj) > len(bj):
        for i in range(len(aj)-len(bj)+1):
            aj_temp = aj[i:i+len(bj)]
            result = max(result, sum([aj_temp[j]*bj[j] for j in range(len(bj))]))
    elif len(aj) < len(bj):
        for i in range(len(bj)-len(aj)+1):
            bj_temp = bj[i:i+len(aj)]
            result = max(result, sum([aj[j]*bj_temp[j] for j in range(len(aj))]))
    print("#" + str(test_case) + " " + str(result))
