
n, l = map(int, input().split())

flag = 0
for i in range(l, 101):
    if i % 2 == 0:
        if (n / i)%1 == 0.5:
            if n//i-(i//2) < -1:
                continue
            flag = 1
            for j in range(n//i-(i//2)+1, n//i + (i//2)+1):
                print(j, end=" ")
            break
    else:
        if n % i == 0:
            if n//i-(i//2) < 0:
                continue
            flag = 1
            for j in range(n//i-(i//2), n//i + (i//2)+1):
                print(j, end=" ")
            break
if flag == 0:
    print(-1)