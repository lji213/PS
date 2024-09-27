n = int(input())

people = [True]*n

arr = []


for i in range(n):
    temp = (input())
    temparr = []
    for j in range(n):
        if temp[j] == "Y":
            temparr.append(j)
    arr.append(temparr)

queue = []

top = 0
count = 0

for i in range(n):
    count = 0
    people = [True]*n
    people[i] = False
    queue = []
    for j in arr[i]:
        count += 1
        people[j] = False
        queue.append(j)

    for j in queue:
        for k in arr[j]:
            if people[k] == True:
                count += 1
                people[k] = False
    top = max(top, count)
    

print(top)