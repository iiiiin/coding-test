# 1208
# [S/W 문제해결 기본] 1일차 - Flatten

for test_case in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
    result = max(box) - min(box)
    print(f"#{test_case} {result}")