n = int(input())
arr = list(map(int, input().split()))
result = 2*n + 4*(sum(arr))
for i in range(n-1):
    result -= 2*min(arr[i], arr[i+1])
print(result)