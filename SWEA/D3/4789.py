# 4789
# 성공적인 공연 기획

T = int(input())

for test_case in range(1,T+1):
    audience = input()
    current = int(audience[0])
    needed = 0
    for i in range(1, len(audience)):
        if current < i:
            needed += i - current
            current = i
        current += int(audience[i])
    print(f"#{test_case} {needed}")