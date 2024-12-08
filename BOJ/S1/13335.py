# 13335
# 트럭


n, w, L = map(int, input().split())
truckweight = list(map(int, input().split()))
bridge = []
t = 0
for i in range(n):
    if i == 0:
        bridge.append(truckweight[i])
        t += (w+1)
    elif len(bridge) <= w-1 and sum(bridge) + truckweight[i] <= L:
        bridge.append(truckweight[i])
        t += 1
    else:
        bridge = [truckweight[i]]
        t += w
    print(i, t)
print(t)
