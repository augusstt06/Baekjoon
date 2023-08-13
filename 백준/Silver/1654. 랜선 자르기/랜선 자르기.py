import sys

k, n = map(int, sys.stdin.readline().split())

arr = list()
for _ in range(k):
    arr.append(int(input()))

arr.sort()

def sol(arr, n, answer):
    start = 1
    end = arr[-1]
    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in arr:
            sliceNum = i // mid
            count += sliceNum

        if n > count:
            end = mid - 1
        if n <= count:
            start = mid + 1
            answer = mid

    return print(answer)

sol(arr, n, 0)

