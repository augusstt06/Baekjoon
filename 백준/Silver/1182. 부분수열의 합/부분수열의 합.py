import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
count = 0


def sol(index, sum):
    global count

    if (index >= n):
        return

    sum += arr[index]
    if (sum == s):
        count += 1
    sol(index + 1, sum)
    sol(index + 1, sum - arr[index])


sol(0, 0)
print(count)
