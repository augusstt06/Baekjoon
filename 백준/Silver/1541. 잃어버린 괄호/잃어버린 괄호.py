n = input()
num = ''
answer = 0
for i in n:
    if i != '-' and i != '+':
        num += i
    elif i == '-':
        answer += int(num)
        num = '-'
    elif i == '+' and num[0] == '-':
        answer += int(num)
        num = '-'
    elif i == '+' and num[0] != '-':
        answer += int(num)
        num = ''
answer += int(num)
print(answer)