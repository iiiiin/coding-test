# 1244

n = int(input())
swt = list(map(int, input().split()))
students = int(input())
for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(len(swt)):
            if (i+1) % num == 0:
                if swt[i] == 1:
                    swt[i] = 0
                else:
                    swt[i] = 1

    elif gender == 2:
        for i in range(min(n-num, num-1)+1):
            if swt[num-1-i] == swt[num-1+i] == 0:
                swt[num-1-i] = 1
                swt[num-1+i] = 1
            elif swt[num-1-i] == swt[num-1+i] == 1:
                swt[num-1-i] = 0
                swt[num-1+i] = 0
            else:
                break

for i in range(len(swt)//20+1):
    print(*swt[20*i:20*(i+1)])