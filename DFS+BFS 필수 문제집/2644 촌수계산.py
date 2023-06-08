"""
입력
전체 사람의 수 n
촌수를 계산해야 하는 사람 
관계 개수 m번
부모 자식의 관계 x y 
"""
import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
g = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
# 서로 연관이 있으니 index는 value들과 연결되어 있다!
visited = [False for _ in range(n+1)]
result = []


def dfs(x, cnt):
    visited[x] = True
    cnt += 1
    for i in g[x]:
        if i == y:
            result.append(cnt)
        elif visited[i] == True:
            continue
        dfs(i, cnt)


dfs(x, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0])
