import sys
input = sys.stdin.readline

def bin(w, s, e):
    mid = (s+e)//2
    if s >= e:
        return mid
    
    if container[3][mid] < w:
        return bin(w, mid+1, e)
    else:
        return bin(w, s, mid)

def find( ):
    count = container[0][-1]+container[1][-1]+container[2][-1]
    for a in range(num[0]):
        count -= container[0][a-1]
        count += container[0][a]
        for b in range(num[1]):
            count -= container[1][b-1]
            count += container[1][b]
            for c in range(num[2]):
                count -= container[2][c-1]
                count += container[2][c]
                if container[3][0] <= -count <= container[3][-1]:
                    if container[3][bin(-count,0,max(num)-1)] == -count:
                        return [container[0][a], container[1][b], container[2][c], -count]



num = list(map(int, input().split()))
container = [[0]*num[0], [0]*num[1], [0]*num[2], [0]*num[3]]



for i in range(4):
    for j in range(num[i]):
        container[i][j] = int(input())

change = [0,0,0]

for i in range(3):
    if num[i] > num[i+1]:
        num[i], num[i+1] = num[i+1], num[i]
        container[i], container[i+1] = container[i+1][:], container[i][:]
        change[i] = 1


container[3].sort()

res = find()

for i in range(2,-1,-1):
    if change[i]:
        res[i], res[i+1] = res[i+1], res[i]

for i in res:
    print(i, end=" ")