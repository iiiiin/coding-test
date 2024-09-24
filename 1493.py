# 1493
# 수의 새로운 연산


als = []
x = 1
k = 0
n = 300
for i in range(n):
    temp = []
    x += i
    u = x
    temp.append(u)
    for j in range(2+k,n+1+k):
        temp.append(u+j)
        u = u+j
    als.append(temp)
    k += 1

T = int(input())

for test_case in range(1,T+1):
    cnt = 0
    p, q = map(int, input().split())
    for i in range(n):
        for j in range(n):
            if als[i][j] == p:
                p_x = i+1
                p_y = j+1
                cnt += 1
            if als[i][j] == q:
                q_x = i+1
                q_y = j+1
                cnt += 1
            if cnt == 2:
                break
    vx = p_x + q_x
    vy = p_y + q_y
    result = als[vx-1][vy-1]
    print(f"#{test_case} {result}")
