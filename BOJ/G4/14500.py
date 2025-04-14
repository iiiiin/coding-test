# 14500
# 테트로미노

'''
완전탐색
'''


import sys
input = sys.stdin.readline

# 일자
def poly1():
    max_v = 0
    for i in range(N):
        for j in range(M-3):
            max_v = max(max_v, sum(paper[i][j:j+4]))
    for i in range(N-3):
        for j in range(M):
            temp = 0
            for k in range(4):
                temp += paper[i+k][j]
            max_v = max(max_v, temp)
    return max_v

# 사각형
def poly2():
    max_v = 0
    for i in range(N-1):
        for j in range(M-1):
            temp = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]
            max_v = max(max_v, temp)

    return  max_v

# L자
def poly3():
    max_v = 0
    # L, 뒤집은 L, ㄱ, 뒤집은 ㄱ
    for i in range(N-2):
        for j in range(M-1):
            temp1 = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
            temp2 = paper[i][j+1] + paper[i + 1][j+1] + paper[i + 2][j] + paper[i + 2][j + 1]
            temp3 = paper[i][j+1] + paper[i + 1][j+1] + paper[i][j] + paper[i + 2][j + 1]
            temp4 = paper[i][j+1] + paper[i + 1][j] + paper[i][j] + paper[i + 2][j]
            max_v = max(max_v, temp1, temp2, temp3, temp4)
    # ㄴ, ㄱ 뒤집은 ㄴ, ㄱ
    for i in range(N-1):
        for j in range(M-2):
            # ㄴ
            temp1 = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
            # ㄱ
            temp2 = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
            # 뒤집은 ㄴ
            temp3 = paper[i][j+2] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
            # 뒤집은 ㄱ
            temp4 = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j]
            max_v = max(max_v, temp1, temp2, temp3, temp4)

    return max_v

# 번개
def poly4():
    max_v = 0
    # 세로 번개
    for i in range(1, N-1):
        for j in range(M-1):
            # ㄴㄱ
            temp1 = paper[i][j] + paper[i-1][j] + paper[i][j+1] + paper[i+1][j+1]
            # 뒤집은 ㄴㄱ
            temp2 = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i-1][j+1]
            max_v = max(max_v, temp1, temp2)

    # 가로 번개
    for i in range(N-1):
        for j in range(1, M-1):
            # ㄱㄴ
            temp1 = paper[i][j-1] + paper[i][j] + paper[i+1][j] + paper[i+1][j+1]
            # 뒤집은 ㄱㄴ
            temp2 = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+1][j-1]
            max_v = max(max_v, temp1, temp2)
    return max_v

# ㅜ
def poly5():
    max_v = 0
    # ㅜ, ㅗ
    for i in range(N-1):
        for j in range(1, M-1):
            # ㅜ
            temp1 = paper[i][j-1] + paper[i][j] + paper[i][j+1] + paper[i+1][j]
            # ㅗ
            temp2 = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+1][j+1]
            max_v = max(max_v, temp1, temp2)

    # ㅏ, ㅓ
    for i in range(1, N - 1):
        for j in range(M - 1):
            # ㅏ
            temp1 = paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j+1]
            # ㅓ
            temp2 = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i+1][j+1]
            max_v = max(max_v, temp1, temp2)

    return max_v

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
print(max(poly1(),poly2(),poly3(),poly4(),poly5()))
