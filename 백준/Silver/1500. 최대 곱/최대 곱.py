import sys

s, k = map(int, sys.stdin.readline().split())
temp = s//k
m = s % k
answer = 1

for _ in range(k):
    if (m > 0):
        answer *= temp + 1
        m -= 1
    else:
        answer *= temp
print(answer)
