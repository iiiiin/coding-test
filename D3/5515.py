# 5515
# 2016년 요일 맞추기



T = int(input())
for test_case in range(1,T+1):
    mth = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = [4,5,6,0,1,2,3]
    m, d = map(int, input().split())
    result = days[(sum(mth[:m - 1])+d-1) % 7]
    print(f"#{test_case} {result}")
