# 1343
# 폴리오미노

polyomino = input()

s = polyomino.split('.')
s = [x for x in s if x]
dots = polyomino.split('X')
dots = [x for x in dots if x]

len_s = len(s)
len_dots = len(dots)

result = 0

for i in range(len(s)):
    if len(s[i]) % 2 == 0:
        result = 1
        if len_s == len_dots - 1:
            if i == len_s - 1:
                s[i] = dots[i] + "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2) + dots[i+1]
                continue
            s[i] = dots[i] + "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2)
        elif len_s == len_dots + 1:
            if i == len_s - 1:
                s[i] = "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2)
                continue
            s[i] = "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2) + dots[i]
            
        elif len_s == len_dots:
            if polyomino[0] == ".":
                s[i] = dots[i] + "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2)
            else:
                s[i] = "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2) + dots[i]
        else:
            s[i] = "AAAA" * (len(s[i]) // 4) + "BB" * ((len(s[i]) % 4) // 2)
    else: 
        result = -1
        break
        
if result == -1:
    print(result)
elif result == 1:
    print("".join(s))
else:
    print(polyomino)