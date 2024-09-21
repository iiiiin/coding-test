# 14692
# 통나무 자르기

TC = int(input())

for test_case in range(1,TC+1):
    n = int(input())
    if n % 2 == 0:
        result = "Alice"
    else:
        result = "Bob"
    print(f"#{test_case} {result}")