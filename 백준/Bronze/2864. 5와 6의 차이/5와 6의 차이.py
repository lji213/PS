a, b = input().split()

a = list(map(int, list(a)))
b = list(map(int, list(b)))

mini = 0
maxi = 0

for i in range(len(a)):
    if a[-i-1] == 5:
        maxi += 10**(i)
    elif a[-i-1] == 6:
        mini -= 10**(i)
    mini += 10**(i)*a[-i-1]
    maxi += 10**(i)*a[-i-1]

for i in range(len(b)):
    if b[-i-1] == 5:
        maxi += 10**(i)
    elif b[-i-1] == 6:
        mini -= 10**(i)
    mini += 10**(i)*b[-i-1]
    maxi += 10**(i)*b[-i-1]

print(mini, maxi)