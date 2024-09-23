# 3499
# 퍼펙트 셔플

T = int(input())

for test_case in range(10):
    n = int(input())
    s = list(input().split())
    result = ""
    if n % 2 == 0:
        first = s[:n//2]
        second = s[n//2:]
    else:
        first = s[:n//2+1]
        second = s[n//2+1:]
    for i in range(len(second)):
        result += first[i] + " "
        result += second[i] + " "
    if len(first) > len(second):
        result += first[-1]
    print(f"#{test_case} ", end="")
    print(result.rstrip())