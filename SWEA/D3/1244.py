# 1244
# [S/W 문제해결 응용] 2일차 - 최대 상금

def find_max_price(idx, cnt):
    global result
    # 교환 횟수를 모두 사용한 경우
    if cnt == N:
        result = max(result, int(''.join(reward)))
        return
    # 모든 자리의 스왑을 시도한 경우
    if idx == len(reward):
        # 남은 스왑 횟수
        remain = N - cnt
        # 만약 남은 횟수가 홀수이고 모든 숫자가 유일하다면
        if remain % 2 == 1 and len(set(reward)) == len(reward):
            # 마지막 두 숫자를 한 번 교환한 결과를 고려합니다.
            reward[-1], reward[-2] = reward[-2], reward[-1]
            result = max(result, int(''.join(reward)))
            reward[-1], reward[-2] = reward[-2], reward[-1]  # 원상복구
        else:
            result = max(result, int(''.join(reward)))
        return

    # 현재 자리 이후의 모든 자리와 스왑을 시도
    for x in range(idx+1, len(reward)):
        reward[idx], reward[x] = reward[x], reward[idx]
        find_max_price(idx+1, cnt+1)
        reward[idx], reward[x] = reward[x], reward[idx]
    find_max_price(idx+1, cnt)

T = int(input())

for tc in range(1, T+1):
    reward, N = input().split()
    N = int(N)
    reward = list(reward)
    result = 0
    find_max_price(0, 0)
    print(f'#{tc} {result}')
