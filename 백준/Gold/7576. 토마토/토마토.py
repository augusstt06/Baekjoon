from collections import deque

n, m = map(int, input().split())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

visited = list()
for z in range(m):
    visited.append([0] * n)

answer = 0
index_list = list()
possible = True
que = deque()

def sol(que):
    global answer
    while que:
        for _ in range(len(que)):
            y, x = que.popleft()
            visited[y][x] = 1
            for j in range(4):
                ny = y + dy[j]
                nx = x + dx[j]
                if m > ny >= 0 and n > nx >= 0 and visited[ny][nx] == 0 and arr[ny][nx] == 0:
                    que.append([ny, nx])
                    visited[ny][nx] = 1
        answer += 1
    return answer


for s in range(m):
    for q in range(n):
        if arr[s][q] == 1:
            que.append([s,q])
sol(que)

for h in range(m):
    for v in range(n):
        if arr[h][v] == -1:
            visited[h][v] = 1
        if visited[h][v] == 0:
            possible = False
            break
if possible:
    print(answer - 1)
else:
    print(-1)