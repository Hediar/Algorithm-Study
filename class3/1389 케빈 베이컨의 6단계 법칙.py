import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  # n- 유저수, m-친구 관계의 수
g = [[] for _ in range(n+1)]  # index가 친구의 번호
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

# 모든 유저의 케빈 베이컨 수
result = []

# BFS


def bfs(v):
    # v : 시작 index
    queue = deque([v])  # 시작 index
    visited[v] = 1  # 모든값이 0으로 초기화된 크기가 n인 배열에서, v번째값은 1이다.

    while queue:  # queue가 empty할때까지 계속 반복문을 돌릴거다

        # target : 인덱스
        # g[target] : 친구배열
        target = queue.popleft()  # 일단 처음엔 v가 빠져. 그 후에는 '먼저 들어온애'가 빠져
        for i in g[target]:
            # 친구 index
            # visited == 0 : 아예방문 안한거. visited는 거리인거같아(추측)
            if not visited[i]:

                visited[i] = visited[target] + 1  # 1 = 연결되어 있다 = 거리가 1칸이다
                queue.append(i)


for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited))  # i 기준으로 거리

print(result.index(min(result)) + 1)
