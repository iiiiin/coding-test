# 5789
# 현주의 상자 바꾸기

T = int(input())

for test_case in range(1,T+1):
    n, q = map(int, input().split())
    box = [0]*n
    for i in range(1,q+1):
        l, r = map(int, input().split())
        box[l-1:r] = [i]*(r-l+1)
    print(f"#{test_case} ", end="")
    print(*box)