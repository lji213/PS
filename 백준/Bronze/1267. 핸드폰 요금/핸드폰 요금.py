n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    arr[i] += 1

y = 0
m = 0


for i in range(n):
    y += arr[i]//30*10
    if arr[i] % 30:
        y += 10
    m += arr[i]//60*15
    if arr[i] % 60:
        m += 15

if y == m:
    print("Y M", y)
elif y > m:
    print("M", m)
else:
    print("Y", y)