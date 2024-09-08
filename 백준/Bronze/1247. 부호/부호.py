import sys

input = sys.stdin.readline

for _ in range(3):
    count = 0
    for i in range(int(input())):
        count += int(input())
    if count > 0:
        print("+")
    elif count == 0:
        print(0)
    else:
        print("-")
    