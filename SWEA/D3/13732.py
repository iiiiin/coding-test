# 13732
# 정사각형 판정

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    square = [input() for _ in range(n)]
    
    # (1) 정사각형 예측 테이블 초기화
    #     max 값으로 전체 테이블 생성
    visited = [[False]*20 for _ in range(20)]

    # 시작점(x,y) 한 변의 길이(cnt) 변수 초기화
    x,y,cnt = 0,0,0

    # (2) 원본 테이블을 확인하여 정사각형 설정
    for i in range(n):
        flag = 0
        for j in range(n):
            if square[i][j] == "#":
                x = i
                y = j
                while j < n and square[i][j] == "#":
                    j += 1
                    cnt += 1
                flag = 1
                break
        if flag == 1:
            break

    toend = 0
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            if i >= n or j >= n or square[i][j] != "#":
                toend = 1
                break
            visited[i][j] = True
        if toend == 1:
            break

    # (3) 정사각형 비교
    if toend == 1:
        result = "no"
    else:
        for i in range(n):
            result = "yes"
            flag = 0
            for j in range(n):
                if visited[i][j]==False and square[i][j]=="#":
                    flag = 1
                    break
            if flag == 1:
                result = "no"
                break
    
    print(f"#{test_case} {result}")