import sys

str_in = list(sys.stdin.readline().rstrip())
str_out = list()
m = int(sys.stdin.readline())


for _ in range(m):
    command = sys.stdin.readline().split()

    if ((command[0] == 'L') and str_in):
        str_out.append(str_in.pop())
    elif ((command[0] == 'D') and str_out):
        str_in.append(str_out.pop())
    elif ((command[0] == 'B') and str_in):
        str_in.pop()
    elif (command[0] == 'P'):
        str_in.append(command[1])
print("".join(str_in + list(reversed(str_out))))