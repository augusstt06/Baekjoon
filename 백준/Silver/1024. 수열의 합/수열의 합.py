import sys

n, l = map(int, sys.stdin.readline().split())

for i in range(l, 101):
    x = n - (i * (i + 1) / 2)
    if (x % i == 0):
        x = int(x / i)
        if (x + 1) >= 0:
            for j in range(1, i + 1):
                print(x + j, end=' ')
            print()
            break
else:
    print(-1)
