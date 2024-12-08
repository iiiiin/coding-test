# 1181
# 단어 정렬

n = int(input())
a = [input() for x in range(n)]
a = list(set(a))
a = sorted(a,key=lambda x : (len(x),x))
print(*a,sep='\n')