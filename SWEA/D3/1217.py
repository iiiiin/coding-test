# 1217
# [S/W 문제해결 기본] 4일차 - 거듭제곱

def power(x, y, p, cnt):
    # 종료조건
    if p <= cnt:
        return y
    y *= x
    cnt += 1

    # 재귀함수 실행
    return power(x, y, p, cnt)

for test_case in range(10):
    test = int(input())
    n, m = map(int, input().split())
    result = power(n, n, m, 1)
    print(f"#{test} {result}")