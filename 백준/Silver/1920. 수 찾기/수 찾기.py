import sys

n = int(sys.stdin.readline())
note1 = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
note2 = list(map(int,sys.stdin.readline().split()))
for j in note2:
    if j in note1:
        print(1)
    else:
        print(0)