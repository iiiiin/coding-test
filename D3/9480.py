# 9480
# 민정이와 광직이의 알파벳 공부

def generate_combinations(lst):
    result = []
    
    def dfs(index, current_combination):
        result.append(current_combination[:])
        
        for i in range(index, len(lst)):
            current_combination.append(lst[i])
            dfs(i + 1, current_combination)
            current_combination.pop()
    
    dfs(0, [])
    return result[1:]  # 공집합 제외


T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    words = [input().lower() for i in range(n)]
    result = ["".join(x) for x in generate_combinations(words)]
    cnt = 0
    for k in result:
        flag = 0
        for i in range(97,123):
            if chr(i) not in k:
                flag = 1
                break
            else:
                i += 1
        if flag == 0:
            cnt += 1
    print(f"#{test_case} {cnt}")
