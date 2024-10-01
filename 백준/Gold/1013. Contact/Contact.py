import sys
import re
input = sys.stdin.readline

n = int(input())
for i in range(n):
    now = input()[:-1]
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(now)
    if m:
        print("YES")
    else:
        print("NO")
