# 19185
# 육십갑자

T = int(input())

for test_case in range():
    n,m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    result = []
    for _ in range(q):
        k = int(input())
        result.append("".join([s[k%n-1],t[k%m-1]]))
    print(f"#{test_case} ", end="")
    print(*result)