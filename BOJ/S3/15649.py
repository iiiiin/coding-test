# 15649
# N과 M (1)

from itertools import permutations

n, m = map(int, input().split())
result = list(permutations(range(1,n+1), m))
for x in result:
    print(*x)