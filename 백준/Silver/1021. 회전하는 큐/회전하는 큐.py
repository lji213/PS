n, m = map(int, input().split())
want = list(map(int, input().split()))

arr = [i for i in range(1,n+1)]

front = 0
behind = 0

count = 0

for i in want:
    if arr[0] == i:
        arr.pop(0)
    else:
        for j in range(n):
            if arr[j] == i:
                front = j
                break
        for j in range(n):
            if arr[-j] == i:
                behind = j

        if front < behind:
            count += front
            for j in range(front):
                arr.append(arr.pop(0))
        else:
            count += behind
            for j in range(behind):
                arr = [arr[-1]]+arr[:-1]
        arr.pop(0)
    n -= 1
print(count)