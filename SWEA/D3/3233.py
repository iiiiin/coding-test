# 3233
# 정삼각형 분할 놀이

T = int(input())

for test_case in range(1,T+1):
    a, b = map(int, input().split())
    result = (a//b)**2
    print(f"#{test_case} {result}")

"""
A = 4, B = 2, ans = 4
A = 4, B = 1, ans = 4*4
A = 3, B = 1, ans = 
"""