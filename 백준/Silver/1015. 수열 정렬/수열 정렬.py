import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

res = [0]*n

min = 1000
for i in range(n):
    min = 1001
    idx = 0
    for j in range(n):
        if arr[j] < min:
            min = arr[j]
            idx = j
    res[idx] = i
    arr[idx] = 1001
for i in res:
    print(i, end=" ")