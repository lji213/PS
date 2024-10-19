def go():
    global score
    if base == [True]*3:
        score += 1
    for i in range(3):
        if base[i] == False:
            base[i] = True
            break

n = int(input())

arr = list(map(int, input().split()))

score = 0

base = [False]*3

ball = 0


for i in arr:
    if i == 1:
        ball += 1
    elif i == 2:
        ball = 0
        go()
    else:
        ball += 1
        if base[2] == True:
            score += 1
        base[2], base[1], base[0] = base[1], base[0], False
    if ball == 4:
        ball = 0
        go()
    
print(score)