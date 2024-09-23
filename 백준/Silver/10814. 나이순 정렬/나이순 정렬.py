import sys

input = sys.stdin.readline

n = int(input())

arr = [[0, i, ""] for i in range(n)]

for i in range(n):
    a, b = input().split()
    arr[i] = [int(a), i, b]

arr.sort()

for i in arr:
    print(i[0], i[2])