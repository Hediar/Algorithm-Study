from collections import deque


def check(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        # 네 방향 위치 확인
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:  # g범위 벗어날 경우
            continue
        if g[nx][ny] == 1:
            g[nx][ny] = 0  # 방문!
            queue.append((nx, ny))


def bfs(x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        check(x, y)


T = int(input())

for _ in range(T):
    # 가로 m, 세로n, 배추 위치 k
    m, n, k = map(int, input().split())
    g = [[0]*m for _ in range(n)]
    # 입력받는 배추 위치
    for _ in range(k):
        y, x = map(int, input().split())
        g[x][y] = 1

    # BFS로 지렁이가 필요한 수 계산
    queue = deque()
    cnt = 0
    # 밭의 각 좌표를 탐색 했을 때,
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:  # 배추가 있다면?
                bfs(i, j)  # 탐색 시작, 인접 배추들은 0이 되니까
                cnt += 1  # 지렁이 수 count
    print(cnt)
