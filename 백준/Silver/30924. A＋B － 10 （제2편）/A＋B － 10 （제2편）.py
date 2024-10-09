import random
arr = [i for i in range(1, 10001)]
random.shuffle(arr)
for i in arr:
    print("? A", i, flush=True)
    ans = int(input())
    if ans == 1:
        a = i
        break
random.shuffle(arr)
for i in arr:
    print("? B", i, flush=True)
    ans = int(input())
    if ans == 1:
        b = i
        break
print("!", a + b)