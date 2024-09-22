# 5162
# 두가지 빵의 딜레마

T = int(input())

for test_case in range(1,T+1):
    a, b, c = map(int, input().split())
    result = c // (min(a,b))
    print(f"#{test_case} {result}")