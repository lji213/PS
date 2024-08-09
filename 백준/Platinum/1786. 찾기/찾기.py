import sys

input = sys.stdin.readline

t = input()[:-1]
p = input()[:-1]

t_length = len(t)
p_length = len(p)

arr = [-1]+[0]*(p_length)

i = -1
j = 0

while j < p_length:
    if p[i] == p[j] or i == -1:
        i += 1
        j += 1
        arr[j] = i
    else:
        i = arr[i]

count = 0

res = [0]*(t_length-p_length+1)

arr[0] = 0

i = 0
j = 0
while i < t_length:
    if t[i] == p[j]:
        i += 1
        j += 1
        if j == p_length:
            j = arr[j]
            res[count] = i
            count += 1
    else:
        if j == 0:
            i += 1
        else:
            j = arr[j]


print(count)
for i in range(count):
    print(res[i]-p_length+1, end=" ")