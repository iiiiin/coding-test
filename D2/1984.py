# 1984
# 중간 평균값 구하기

T = int(input())

for test_case in range(1,T+1):
    numb = list(map(int, input().split()))
    numb.remove(max(numb))
    numb.remove(min(numb))
    print(f"#{test_case} {round(sum(numb)/len(numb))}")