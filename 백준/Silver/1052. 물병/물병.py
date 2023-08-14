import sys

n, k = map(int, sys.stdin.readline().split())

ans = 0

while (bin(n).count('1') > k):
    n += 1
    ans += 1
print(ans)
