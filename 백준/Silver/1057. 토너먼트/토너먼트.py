n, a, b = map(int, input().split())

if a > b:
    a, b = b, a
a -= 1
b -= 1
round = 0
for i in range(n):
    round += 1
    if a//2 == b//2:
        print(round)
        break
    a = a//2
    b = b//2