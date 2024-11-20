# 1216
# [S/W 문제해결 기본] 3일차 - 회문2

for test_case in range(1,11):
    n = int(input())
    s = [input() for _ in range(100)]
    temp = []
    
    for i in range(100):
        flag = 0
        for j in range(100,-1,-1):
            for k in range(100-j+1):
                if s[i][k:k+j] == s[i][k:k+j][::-1]:
                    temp.append(j)
                    flag = 1
                    break
            if flag == 1:
                break

    s = list(zip(*s))

    for i in range(100):
        flag = 0
        for j in range(100,-1,-1):
            for k in range(100-j+1):
                if "".join(s[i][k:k+j]) == "".join(s[i][k:k+j])[::-1]:
                    temp.append(j)
                    flag = 1
                    break
            if flag == 1:
                break
   
    result = max(temp)
    print(f"#{n} {result}")