# 2467 용액

import sys
n = int(sys.stdin.readline())
water = list(map(int, sys.stdin.readline().split()))

result = [0, 1]

Min = 2000000001
for i in range(n-1):
    if water[i] >= 0 and Min > abs(water[i]+water[i+1]):
        Min = abs(water[i]+water[i+1])
        result = [water[i], water[i+1]]
        break
    s = i + 1
    e = n-1
    while s <= e:
        now = (s+e)//2
        if Min > abs(water[i]+water[now]):
            Min = abs(water[i]+water[now])
            result = [water[i], water[now]]
        if water[i] + water[now] < 0:
            s = now + 1
        else:
            e = now - 1
    if Min > abs(water[i]+water[now]):
        Min = abs(water[i]+water[now])
        result = [water[i], water[now]]
print(result[0], result[1])

