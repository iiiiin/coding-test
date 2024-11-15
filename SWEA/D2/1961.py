# 1961
# 숫자 배열 회전

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

ninety = []
one_eighty = []
two_seventy = []

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(str(arr[n-j-1][i]))
    ninety.append("".join(temp))

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(str(arr[n-i-1][n-j-1]))
    one_eighty.append("".join(temp))

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(str(arr[j][n-i-1]))
    two_seventy.append("".join(temp)) 

# print("#"+str(test_case))
for k in range(n):
    print(ninety[k], one_eighty[k], two_seventy[k])