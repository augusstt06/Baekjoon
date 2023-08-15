import sys
n = int(sys.stdin.readline())
hotkey = list()

for _ in range(n):
    arr = list(map(str, sys.stdin.readline().split()))

    register = False
    for i in range(len(arr)):
        if (arr[i][0].upper() not in hotkey):
            hotkey.append(arr[i][0].upper())
            register = True
            arr[i] = '[' + arr[i][0] + ']' + arr[i][1:]
            print(" ".join(arr))
            break
    if (not register):
        for i in range(len(arr)):
            check = False
            for j in range(len(arr[i])):
                if (arr[i][j].upper() not in hotkey):
                    hotkey.append(arr[i][j].upper())
                    register = True
                    check = True
                    arr[i] = arr[i][:j] + '[' + arr[i][j] + ']' + arr[i][j + 1:]
                    print(" ".join(arr))
                    break
            if (check):
                break
    if (not register):
        print(" ".join(arr))