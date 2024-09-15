# 1983
# 조교의 성적 매기기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    n, k = map(int, input().split())
    score_list = []
    score_dict = {}
    for i in range(n):
        a, b, c = map(int, input().split())
        score = 0.35*a + 0.45*b + 0.2*c
        score_list.append(score)
        score_dict[i] = score
    score_list.sort(reverse=True)
    div = n//10
    if score_dict[k-1] in score_list[0:div]:
        result = "A+"
    elif score_dict[k-1] in score_list[div:2*div]:
        result = "A0"
    elif score_dict[k-1] in score_list[2*div:3*div]:
        result = "A-"
    elif score_dict[k-1] in score_list[3*div:4*div]:
        result = "B+"
    elif score_dict[k-1] in score_list[4*div:5*div]:
        result = "B0"
    elif score_dict[k-1] in score_list[5*div:6*div]:
        result = "B-"
    elif score_dict[k-1] in score_list[6*div:7*div]:
        result = "C+"
    elif score_dict[k-1] in score_list[7*div:8*div]:
        result = "C0"
    elif score_dict[k-1] in score_list[8*div:9*div]:
        result = "C-"
    else:
        result = "D-"
    print("#"+str(test_case)+" "+result)