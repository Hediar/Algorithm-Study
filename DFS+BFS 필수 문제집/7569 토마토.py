"""
- 입력
상자의 크기(가로 세로) M, N 상자의 수 H

토마토들의 정보 
1: 익음
0: 안익음
-1: 토마토가 없음 

- 출력
토마토가 다 익는데 최소 걸리는 날 
이미 모든 토마토가 익어있었다면 0 출력
익지 못하는 상황이면 -1 출력 
"""

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)]
          for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

alltomato = True
result = 0  # 토마토 시간


def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):  # 상하좌우 위 아래
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue

            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                q.append((nx, ny, nz))
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = True


for a in range(H):
    for b in range(N):
        for c in range(M):
            if tomato[a][b][c] == 1 and visited[a][b][c] == 0:
                q.append((a, b, c))
                visited[a][b][c] = True
            elif tomato[a][b][c] == 0:  # 하나라도 안익은게 있다면
                alltomato = False
bfs()

for a in tomato:
    for b in a:
        for c in b:
            if c == 0:  # 덜 익은 토마토 확인
                print(-1)
                exit(0)
        result = max(result, max(b))

if alltomato == True:
    print(0)
else:
    print(result-1)
