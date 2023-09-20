import sys
from itertools import combinations
# 중복 없는 조합 이용

n = int(sys.stdin.readline())
answer = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        answer.append(int(num))

answer.sort()

if n >= len(answer):
    print(-1)

else:
    print(answer[n])
