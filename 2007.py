# 2007
# 패턴 마디의 길이

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    s = input()
    s_string = ""
    for i in range(len(s)):
        s_string += s[i]
        if i > 0 and len([x for x in s.split(s_string) if x != ""]) <= 1:
            break
    result = str(len(s_string))
    print("#"+str(test_case)+" "+result)

