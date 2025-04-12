# 1759
# 암호 만들기

'''
주어진 문자로 순열을 만들기
단 조건을 추가하여 사전적 크기 비교
DFS
'''

import sys
input = sys.stdin.readline

def is_valid(lst):
    vowels = 0
    consonants = 0
    for text in lst:
        if text in ['a','e','i','o','u']:
            vowels += 1
        else:
            consonants += 1
        if vowels >= 1 and consonants >= 2:
            return 1
    return 0

def find_pw(temp):
    if len(temp) == L:
        temp = [password[k] for k in temp]
        if is_valid(temp):
            result.append(''.join(temp))
        return
    if not temp:
        for idx in range(C):
            find_pw(temp+[idx])
    else:
        for idx in range(temp[-1], C):
            if idx not in temp:
                find_pw(temp + [idx])


L, C = map(int, input().split())
password = sorted(input().split())
result = []
find_pw([])
result.sort()
for t in result:
    print(t)
