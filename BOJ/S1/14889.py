# 14889
# 스타트와 링크

'''
스타트와 링크, 2 집합으로 나누기
N/2 개의 원소를 가지는 부분집합(조합) 구하기
=> 자동으로 속하지 않는 원소들의 집합 구하기
DFS로 각 조합으로 계산했을 때 최솟값 갱신
=> 시간복잡도 개선 : DFS 실행 시 계산 수행 해서 최솟값 갱신, 부분집합 조합 구하지 않고, 바로 수행
'''

import sys

input = sys.stdin.readline


def get_comb(idx, temp):
    global min_v
    if idx == N:
        if len(temp) == N // 2:
            link = [x for x in range(N) if x not in temp]
            sv = 0
            for i in temp:
                for j in temp:
                    sv += arr[i][j]
            lv = 0
            for i in link:
                for j in link:
                    lv += arr[i][j]
            min_v = min(min_v, abs(sv - lv))

        return
    get_comb(idx + 1, temp + [idx])
    get_comb(idx + 1, temp)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')
get_comb(0, [])

print(min_v)
