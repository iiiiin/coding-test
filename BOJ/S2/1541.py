# 1541
# 잃어버린 괄호

formula = input().split('-')

for i in range(len(formula)):
    if i == 0:
        answer = sum(list(map(int, formula[i].split('+'))))
    else:
        answer -= sum(list(map(int, formula[i].split('+'))))
    
print(answer)