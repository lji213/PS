import sys

input  = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, goal = input().split()
    a = int(a[:3]+a[4:])-144000
    b = int(b[:3]+b[4:])-144000
    goal = int(goal[:3]+goal[4:])-144000

    res = 6

    if c == "A":
        aa = 0
        bb = 1
        now = a
    else:
        now = b
        aa = 0
        bb = 1

    au = a
    ad = a
    bu = b
    bd = b


    for i in range(7):
        if au == goal or ad == goal:
            break
        au += 20
        if au > 2000:
            au = 0

        ad -= 20
        if ad < 0:
            ad = 2000
    aa = i

    for i in range(7):
        if bu == goal or bd == goal :
            break
        bu += 20
        if bu > 2000:
            bu = 0

        bd -= 20
        if bd < 0:
            bd = 2000
    bb = i

    if c == "A":
        bb += 1
    else:
        aa += 1
    res = min(res, aa, bb)
    print(res)