# 1989
# 초심자의 회문 검사

T = int(input())

for test_case in range(1,T+1):
    words = input()
    if words == words[::-1]:
        result = 1
    else:
        result = 0
    print(f"#{test_case} {result}")