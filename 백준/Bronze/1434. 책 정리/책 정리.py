n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))


box += [0]


space = box[0]
nownum = 0
res = 0


i = 0
while i < m:
    if space >= book[i]:
        space -= book[i]
        i += 1
    else:
        nownum += 1
        res += space
        space = box[nownum]


res += space
for i in range(nownum+1, n):
    res += box[i]
print(res)