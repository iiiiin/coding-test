# 4299
# 태혁이의 사랑은 타이밍

T = int(input())

for test_case in range(1,T+1):
    d, h, m = map(int, input().split())
    if any([d < 11, d == 11 and h < 11, d == 11 and h > 11 and m < 11]):
        result = -1
    else:
        result = (d - 11)*24*60+(h-11)*60+m-11
    print(f"#{test_case} {result}")
           