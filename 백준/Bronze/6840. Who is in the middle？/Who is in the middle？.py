import sys
input = sys.stdin.readline
arr = [0, 0, 0]
for i in range(3):
   arr[i] = int(input())
arr.sort()
print(arr[1])