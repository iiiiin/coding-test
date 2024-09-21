# 4751
# 다솔이의 다이아몬드 장식

T = int(input())

for test_case in range(1,T+1):
    s = input()
    print("."+".".join([".#."]*len(s))+".")
    print("."+".".join(["#","#"]*len(s))+".")
    print("#."+".#.".join(list(s))+".#")
    print("."+".".join(["#","#"]*len(s))+".")
    print("."+".".join([".#."]*len(s))+".")
