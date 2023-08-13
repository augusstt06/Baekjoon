from collections import deque

n, k = map(int, input().split())
answer = 0
visited = [0] * 100001
que = deque()
que.append(n)
visited[n] = 1


def sol(que):
    global answer
    while k not in que:
        for _ in range(len(que)):
            v = que.popleft()
            for i in (v + 1, v - 1, v * 2):
                if 0 <= i <= 100000 and visited[i] == 0:
                    que.append(i)
                    visited[i] = 1
        answer += 1


sol(que)
print(answer)