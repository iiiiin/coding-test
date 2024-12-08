# 10828
# 스택

n = int(input())

stack = []

for i in range(n):
    contents = len(stack)
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    
    elif command[0] == "pop":
        if contents == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(contents)
    elif command[0] == "empty":
        if contents == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if contents == 0:
            print(-1)
        else:
            print(stack[-1])
