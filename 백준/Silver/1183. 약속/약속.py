import sys

n = int(sys.stdin.readline())
arr = list()

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a - b)

arr.sort()

if n % 2 == 1:
    print(1)
else:
    answer = abs(arr[n//2] - arr[n//2-1] + 1)
    print(answer)
