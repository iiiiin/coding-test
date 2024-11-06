# 20019
# 회문의 회문

T = int(input())

for test_case in range(1,T+1):
    s = input()
    condition = [s[:len(s)//2+1] == s[len(s)//2:][::-1], 
                 s[:(len(s)-1)//2] == s[:(len(s)-1)//2][::-1],
                 s[((len(s)-1)//2)+1:] == s[((len(s)-1)//2)+1:][::-1]]
    if all(condition):
        result = "YES"
    else:
        result = "NO"
    print(f"#{test_case} {result}")