import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [i for i in range(101)]
visited = [0 for _ in range(101)]

for i in range(N):
    x, y = map(int, input().split())
    graph[x] = y # 사다리 연결

for j in range(M):
    u, v = map(int, input().split())
    graph[u] = v # 뱀 연결

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1 # 맨 처음 위치
    while q:
        x = q.popleft()
        for i in range(1, 7): # 주사위 범위
            nx = x + i
            if nx > 100:
                continue # 100을 넘지 못함!
            cnt = graph[nx]
            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[x] + 1 # 이동했으니 +1
                if cnt == 100:
                    return

bfs()
print(visited[100] - 1)