import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


ans = [0] * n
for i in range(n):
    count = 0
    for j in range(n):
        if (count == arr[i] and ans[j] == 0):
            ans[j] = i + 1
            break
        elif (ans[j] == 0):
            count += 1
print(' '.join(map(str, ans)))
