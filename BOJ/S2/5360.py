# 5360
# Next Permutation

def nextpermutation(a):
    check = 0
    for i in range(len(a)-1,0,-1):
        if a[i-1] < a[i]:
            min_j = i
            for j in range(i+1,len(a)):
                if a[i-1] < a[j] and a[min_j] > a[j]:
                    min_j = j
            a[i-1], a[min_j] = a[min_j], a[i-1]
            a[i:] = sorted(a[i:])
            a = "".join(a)
            check = 1
            break
    if check == 0:
        print("USELESS")
    else:
        print(a)
    return 0

n = int(input())

for k in range(n):
    a = list(input())
    nextpermutation(a)