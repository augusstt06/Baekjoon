import sys

n = int(sys.stdin.readline().rstrip())
arr = list()

for i in range(n):
    arr.append(sys.stdin.readline().strip())

arr.sort(key=len)
ans = 0

for i in range(n):
    isPre = False
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j][:len(arr[i])]):
            isPre = True
            break
    if not isPre:
        ans += 1
print(ans)
