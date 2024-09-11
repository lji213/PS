a, b = map(int, input().split())

arr = []

for i in range(50):
    arr += [i+1]*(i+1)

print(sum(arr[a-1:b]))