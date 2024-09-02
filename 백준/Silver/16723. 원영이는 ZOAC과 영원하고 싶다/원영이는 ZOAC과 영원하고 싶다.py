n = int(input())

count = 0
res = 0
na = 2**30


for i in range(31):
    temp = n//na-count
    count += temp
    res += temp*na
    na = na//2



print(res*2)
