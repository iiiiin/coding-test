# 14555
# 공과 잡초

T = int(input())

for test_case in range(1,T+1):
    s = input()
    result = s.count("(|") + s.count("|)") + s.count("()")
    print(f"#{test_case} {result}")