# 4466
# 최대 성적표 만들기

T = int(input())

for test_case in range(1,T+1):
    n, k = map(int, input().split())
    score = sorted(list(map(int, input().split())),reverse=True)
    result = sum(score[:k])
    print(f"#{test_case} {result}")
