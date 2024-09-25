# 3314
# 보충학습과 평균

T = int(input())

for test_case in range(1,T+1):
    score = list(map(int, input().split()))
    score = [x if x >= 40 else 40 for x in score]
    result = sum(score)//5
    print(f"#{test_case} {result}")