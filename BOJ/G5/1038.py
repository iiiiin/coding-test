# 1038
# 감소하는 수

'''
풀이참고
감소하는 모든 수 조합 구하기
그리고 감소하도록 내림차순 정렬
그리고 모든 수들을 오름차순 정렬
감소하는 수 : 각 자릿수가 같지 않고, 오른쪽으로 갈수록 감소
최대 감소하는 수 => 9876543210
'''

from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())

# 감소하는 수 리스트
dec_num = []
# 1자리부터 10자리수까지 조합
for i in range(1,11):
    # 0 ~ 9까지 수 중 i개로 구성된 조합
    for j in combinations(range(10), i):
        dec_num.append(int(''.join(map(str, sorted(j, reverse=True)))))
dec_num.sort()
if N >= len(dec_num):
    print(-1)
else:
    print(dec_num[N])


