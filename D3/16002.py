# 16002
# 합성수 방정식

# x, y가 합성수인지 확인하는 함수
def chk(num):
    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return True
    return False

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    x = 4
    # x, x+n을 만족하는 x 값을 확인
    # x, y(x+n)의 함수가 모두 True 일 때, 반복문 중단
    while True:
        if chk(x) and chk(x+n):
            break
        x += 1
    print(f"#{test_case} {x+n} {x}")