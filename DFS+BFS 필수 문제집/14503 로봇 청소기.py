"""
입력 
방크기 n, m
청소기의 좌표 r, c
바라보는 방향 d
북 - 0, 동 - 1, 남 - 2, 서 - 3 
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())

# 북 서 남 동 순서 0321
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 처음 시작하는 곳 방문처리
visited[r][c] = 1
cnt = 1

while True:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]

        d = (d+3) % 4  # 한바퀴 확인했으면 해당 방향으로 작업 시작

        # 영역 확인, 깨끗한지 확인
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1  # 방문처리
                cnt += 1
                r = nx
                c = ny
                flag = 1
                break
    if flag == 0:  # 4방향 모두 청소가 되어있다면
        if graph[r-dx[d]][c-dy[d]] == 1:  # 후진했을 때 벽이라면
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]  # 이전 위치로 돌아가기
