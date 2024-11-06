# 1486
# 장훈이의 높은 선반

def recur(idx, sumheight, result, n, h):
    # 종료 조건 : 인덱스 범위를 벗어날 때
    # 리스트를 모두 순회 했으므로 고른 원소들의 합 빈 리스트에 추가
    if idx >= n:
        result.append(sumheight)
        return result
    
    # 재귀함수 실행 : 현재 인덱스의 원소를 포함하는 경우
    # 다음 인덱스로 이동하고, 현재 인덱스의 원소를 포함한 값을 입력
    result = recur(idx+1, sumheight + h[idx], result, n, h)
    
    # 재귀함수 실행 : 현재 인덱스의 원소를 포함하지 않는 경우
    result = recur(idx+1, sumheight, result, n, h)
    return result

T = int(input())

for test_case in range(1,T+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    result = min([x for x in recur(0,0,[],n,h) if x >= b]) - b
    print(f"#{test_case} {result}")