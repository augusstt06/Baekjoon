import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)

answer = []


def bfs(start):
    count = 1
    queue = deque([start])
    visit = [False] * (n + 1)
    visit[start] = True

    while queue:
        current = queue.popleft()

        for i in arr[current]:
            if not visit[i]:
                visit[i] = True
                count += 1
                queue.append(i)
    return count


for i in range(1, n + 1):
    answer.append(bfs(i))

max = max(answer)

for i in range(len(answer)):
    if max == answer[i]:
        print(i + 1, end=" ")
