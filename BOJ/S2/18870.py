# 18870
# 좌표 압축

n = int(input())
array = list(map(int, input().split()))
answer = sorted(set(array))
dic = {answer[i] : i for i in range(len(answer))}
for i in array:
    print(dic[i], end = ' ')