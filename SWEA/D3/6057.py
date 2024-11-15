# 6057
# 그래프의 삼각형

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    conn = [set() for _ in range(n+1)]
    
    for _ in range(m):
        x, y = map(int, input().split())
        conn[x].add(y)
        conn[y].add(x)
    
    count = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if j in conn[i]:
                common_neighbors = conn[i] & conn[j]
                count += len(common_neighbors) - (1 if j > i else 0)
    
    print(f"#{test_case} {count}")