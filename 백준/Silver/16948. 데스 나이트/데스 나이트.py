import sys
from collections import deque

input = sys.stdin.readline

dy = [-2, 0, 2, 2, 0, -2]
dx = [1, 2, 1, -1, -2, -1]


def dfs(y, x):
    for i in range(6):
        yy = y+dy[i]
        xx = x+dx[i]
        if 0 <= yy < n and 0 <= xx < n and board[yy][xx] == 0:
            queue.append([yy, xx])
            board[yy][xx] = board[y][x]+1


n = int(input())

y, x, gy, gx = map(int, input().split())

queue  = deque([[y, x]])

board = [[0]*n for _ in range(n)]

board[y][x] = 1

while queue:
    if board[gy][gx]:
        break
    now = queue.popleft()
    dfs(now[0], now[1])


if board[gy][gx]:
    print(board[gy][gx]-1)
else:
    print(-1)