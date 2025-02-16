# 2559
# 수열

# 슬라이딩 윈도우
# 누적합

# 입력받기
n, k = map(int, input().split())
temperature = list(map(int, input().split()))

# 누적합 계산
for i in range(1, n):
    temperature[i] += temperature[i-1] 

# 초기값 설정
result = temperature[k-1]

for i in range(1, n-k+1):
    # 이동한 범위의 합(누적합 차)과 비교하여 최대값 갱신
    temp = temperature[i+k-1] - temperature[i-1]
    result = max(result, temp)

print(result)