import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if graph[nx][ny] == 0: # 갈 수 없는 곳 
                    visited[nx][ny] = 0 
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))



# 탐색!
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1: # 목표지점 & 방문 x일때 bfs
            bfs(i,j)

# 출력
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 목표지점 출력
            print(0, end=' ') 
        else:
            print(visited[i][j], end=' ')
    print() # 줄바꿈