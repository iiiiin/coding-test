# 2491
# 수열

'''
점점 커지는 수열의 길이와 점점 작아지는 수열의 길이를
매 반복마다 비교해서 그 중 큰 값을 리스트에 담고
리스트의 최댓값을 반환
'''

# 입력받기
n = int(input())
arr = list(map(int, input().split()))

# 비교 위한 초기값 설정
smaller_cnt = 1
bigger_cnt = 1
temp = []

# 반복문 실행
for i in range(n-1):
    # 점점 커질 경우
    if arr[i] < arr[i+1]:
        # 지금까지 작아지는 수열을 세었을 경우
        if smaller_cnt:
            # 지금까지 셌던 점점 작아지는 수열 길이 저장
            temp.append(smaller_cnt)
            # 수열 길이 다시 0으로 초기화
            smaller_cnt = 1
        bigger_cnt += 1

    # 점점 작아질 경우
    elif arr[i] > arr[i+1]:
        # 지금까지 커지는 수열을 세었을 경우
        if bigger_cnt:
            # 지금까지 셌던 점점 작아지는 수열 길이 저장
            temp.append(bigger_cnt)
            # 수열 길이 다시 0으로 초기화
            bigger_cnt = 1
        smaller_cnt += 1
    # 이웃한 두 인덱스의 값이 같을 경우
    else:
        # 모두 1씩 증가
        smaller_cnt += 1
        bigger_cnt += 1
# 마지막까지 세었던 값들도 리스트에 추가
temp.append(smaller_cnt)
temp.append(bigger_cnt)
# 최대 길이 출력
print(max(temp))

    
