m = int(input())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input())))

stack = list()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = list()
for v in range(m):
    visited.append([0] * m)

def dfs(x, y, stack):
    stack.append((x,y))
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if m > nx >= 0 and m > ny >= 0 and visited[nx][ny] == 0 and arr[nx][ny] == 1:
            dfs(nx, ny, stack)

    return len(stack)


result = list()
for j in range(m):
    for s in range(m):
        if arr[j][s] == 1 and visited[j][s] == 0:
            stack = list()
            result.append(dfs(j, s, stack))
        elif arr[j][s] == 0 and visited[j][s] == 0:
            visited[j][s] = 1

print(len(result))

for b in sorted(result):
    print(b)