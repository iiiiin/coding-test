# 1221
# [S/W 문제해결 기본] 5일차 - GNS

T = int(input())

for test_case in range(1,T+1):
    num = {"ZRO":0,"ONE":1,"TWO":2,"THR":3,"FOR":4,"FIV":5,"SIX":6,"SVN":7,"EGT":8,"NIN":9}
    tc, n = input().split()
    num_list = list(input().split())
    comp = sorted([num[x] for x in num_list])
    num = {value:key for key,value in num.items()}
    result = [num[x] for x in comp]
    print(tc)
    print(*result)