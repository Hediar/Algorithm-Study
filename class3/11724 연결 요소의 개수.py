import sys
sys.setrecursionlimit(10**6) # 반복문 제한 
input = sys.stdin.readline

n, m = map(int, input().split()) # 정점, 간선의 개수 
g = [[] for _ in range(n+1)]

def dfs(g, v, visited):
    visited[v] = True # 방문 표시
    
    for i in g[v]:

        if not visited[i]:
            dfs(g, i , visited)

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):

    if not visited[i]:
        dfs(g, i, visited)
        cnt+=1

print(cnt)