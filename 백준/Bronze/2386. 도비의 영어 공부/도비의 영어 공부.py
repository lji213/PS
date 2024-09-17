import sys

input = sys.stdin.readline

while True:
    now = input()
    if now[0] == "#":
        break
    count = 0
    for i in now[2:-1]:
        if ord(i) in [ord(now[0]), ord(now[0])-32]:
            count += 1
    print(now[0], count)