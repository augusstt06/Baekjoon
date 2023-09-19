import sys

r, c, k = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline()) for _ in range(r)]
answer = 0


def sol(x, y, p_k):
    global answer

    if p_k == k:
        if (x, y) == (0, c - 1):
            answer += 1
    else:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != 'T':
                arr[nx][ny] = 'T'
                sol(nx, ny, p_k + 1)
                arr[nx][ny] = '.'


arr[r - 1][0] = 'T'
sol(r - 1, 0, 1)
print(answer)
