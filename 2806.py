# 2806
# N-Queen

def is_safe(queens,row,col):
    for r in range(row):
        if queens[r] == col or abs(queens[r]-col) == abs(r-row):
            return False
    return True

def solve_n_queens(n):
    def backtrack(row,queens):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_safe(queens,row,col):
                queens[row] = col
                backtrack(row+1,queens)
                queens[row] = -1
    result = []
    queens = [-1] * n
    backtrack(0,queens)
    return len(result)

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = solve_n_queens(n)
    print(f"#{test_case} {result}")