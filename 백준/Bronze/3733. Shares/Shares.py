import sys
input = sys.stdin.readline
while 1:
   try:
       a, b = map(int, input().split())
       print(b//(a+1))
   except:
       break