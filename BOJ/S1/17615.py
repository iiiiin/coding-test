# 17615
# 볼 모으기

n = int(input())
s = input()

red = s.split('B')
move_red = len("".join(red)) - max(len(red[0]), len(red[-1]))

blue = s.split('R')
move_blue = len("".join(blue)) - max(len(blue[0]), len(blue[-1]))

print(min(move_red, move_blue))