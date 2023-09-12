import sys

n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

connect = [[0] * n for _ in range(n)]

for k in range(n):
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            if (arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y')):
                connect[i][j] = 1

answer = 0

for i in connect:
    answer = max(answer, sum(i))
print(answer)
