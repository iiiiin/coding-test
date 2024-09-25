# 4047
# 영준이의 카드 카운팅

T = int(input())

for test_case in range(1,T+1):
    card = {"S":13,"D":13,"H":13,"C":13}
    s = input()
    flag = 0
    for i in range(0,len(s),3):
        if s.count(s[i:i+3]) > 1:
            result = "ERROR"
            flag = 1
            break
        card[s[i]] -= 1
    if flag == 0:
        result = list(card.values())
    print(f"#{test_case} ", end="")
    if flag == 0:
        print(*result)
    else:
        print(result)