count = 0
m = 0
for i in range(4):
    a, b = map(int, input().split())
    count += -a + b
    m = max(m, count)
print(m)