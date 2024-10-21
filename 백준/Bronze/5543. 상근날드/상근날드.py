b = 2000
for i in range(3):
    b = min(b, int(input()))
d = 2000
for i in range(2):
    d = min(d, int(input()))
print(b+d-50)