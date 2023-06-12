from collections import deque

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input())))


def bfs(x, y):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):  # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘어가지 않도록
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이면 continue 아니라면 카운트 해준다.
            if g[nx][ny] == 0:
                continue

            if g[nx][ny] == 1:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1
    return g[n-1][m-1]


print(bfs(0, 0))
