n, m = map(int, input().split())

arr_a = list()

for _ in range(n):
    arr_a.append(list(map(int, input())))

arr_b = list()
for _ in range(n):
    arr_b.append(list(map(int, input())))

count = 0


def flip_arr(x, y, arr_a):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr_a[i][j] = 1 - arr_a[i][j]


for i in range(n - 2):
    for j in range(m - 2):
        if (arr_a[i][j] != arr_b[i][j]):
            flip_arr(i, j, arr_a)
            count += 1
flag = True
for i in range(n):
    for j in range(m):
        if (arr_a[i][j] != arr_b[i][j]):
            flag = False
            break
if flag != True:
    count = -1

print(count)
