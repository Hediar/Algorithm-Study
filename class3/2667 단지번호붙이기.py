"""
- 입력
지도의 크기 N
줄마다 N개의 자료

- 출력
총 단지수, 각 단지내 집의 수 오름차순으로 
"""

import sys
from collections import deque
input = sys.stdin.readline
"""
n = int(input())

g = [list(map(int, input().rstrip())) for _ in range(n)]


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    cnt = 1
    q = deque()
    q.append((x, y))

    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


result = []

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            result.append(bfs(g, i, j))

result.sort()
print(len(result))

for i in range(len(result)):
    print(result[i])
"""

n = int(input())

g = [list(map(int, input().rstrip())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(g, x, y):
    cnt = 1
    q = deque()
    q.append((x, y))

    g[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벗어나지 않게 범위 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if g[nx][ny] == 1:
                cnt += 1
                g[nx][ny] = 0  # 갔던곳은 다시 못가게 0으로
                q.append((nx, ny))
    return cnt


result = []

# 1의 처음 좌표를 찾아주어야 함

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            result.append(bfs(g, i, j))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
