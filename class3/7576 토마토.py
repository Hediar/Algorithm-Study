from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]


q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


alltomato = True
result = 0  # 토마토 시간


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):  # 상하좌우 위 아래
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue

            if tomato[nx][ny] == 0:
                q.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1



for a in range(N):
    for b in range(M):
        if tomato[a][b] == 1:
            q.append((a, b))

        elif tomato[a][b] == 0:  # 하나라도 안익은게 있다면
            alltomato = False
bfs()

for a in tomato:
    for b in a:
        if b == 0:  # 덜 익은 토마토 확인
            print(-1)
            exit(0)
    result = max(result, max(a))


print(result-1)
