import sys
tmep = input()
f = int(input())
n = int(tmep[:-2])*100
for i in range(100):
    if (n+i)%f == 0:
        if i < 10:
            print("0", end="")
        print(i)
        break