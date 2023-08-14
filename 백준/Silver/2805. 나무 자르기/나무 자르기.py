import sys
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

def sol(arr, m):
    start = 0
    end = arr[-1]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        length = 0

        for i in arr:
            if i <= mid:
                length += 0

            else:
                length += i - mid

        if length >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return print(answer)

sol(arr, m)
