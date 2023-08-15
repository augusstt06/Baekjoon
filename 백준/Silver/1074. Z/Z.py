import sys

n, r, c = map(int, sys.stdin.readline().split())
ans = 0


def sol(n, x, y):
    global ans
    if (x == r and y == c):
        print(int(ans))
        return
    if (n == 1):
        ans += 1
        return
    if not (x <= r < x+n and y <= c < y+n):
        ans += n * n
        return
    sol(n / 2, x, y)
    sol(n / 2, x, y + n / 2)
    sol(n / 2, x + n / 2, y)
    sol(n / 2, x + n / 2, y + n / 2)


sol(2 ** n, 0, 0)
