import sys

a, b = map(int, sys.stdin.readline().split())

arr = [0] * (b + 1)
prime_arr = [False] * (b+1)
answer = 0


def is_underPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            arr[n] = arr[n//i] + 1
            return False
    arr[n] = 1
    return True


for i in range(2, b + 1):
    prime_arr[i] = is_underPrime(i)

for i in range(a, b + 1):
    answer += prime_arr[arr[i]]

print(answer)
