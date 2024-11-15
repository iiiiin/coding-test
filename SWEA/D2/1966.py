# 1966
# 숫자를 정렬하자

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = sorted(list(map(int, input().split())))
    result = [str(result[x]) for x in range(len(result))]
    print("#"+str(test_case)+" "+" ".join(result))