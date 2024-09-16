# 2005
# 파스칼의 삼각형

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    temp = []
    for i in range(1,N+1):
        temp.append([1]*i)
    
    for j in range(N):
        if j > 1:
            for k in range(len(temp[j-1])-1):
                temp[j][k+1] = temp[j-1][k]+temp[j-1][k+1]
        
    print(f"#{test_case}")
    for a in range(N):
        print(*temp[a])
    
