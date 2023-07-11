import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g=[]
max_height = 0

for _ in range(n):
    g.append(list(map(int, input().split())))
    max_height = max(max_height, max(g[-1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,r):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

result = 0
for i in range(max_height):
    cnt = 0
    visited = [[0]*n for _ in range(n)]