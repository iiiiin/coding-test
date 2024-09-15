# 1288
# 새로운 불면증 치료법


T = int(input())
for test_case in range(1, T+1):
    zero_to_nine = list(map(str, range(10)))
    n = int(input())
    cnt = 1
    origin_num = n
    while True:
        n = str(n)
        for i in range(len(n)):
            test_num = int(n[i])
            if zero_to_nine[test_num] == str(test_num):
                zero_to_nine[test_num] = ""
            result = n
        cnt += 1
        n = origin_num * cnt

        if len("".join(zero_to_nine)) == 0:
            break

    print("#"+str(test_case)+" "+result)