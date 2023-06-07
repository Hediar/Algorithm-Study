"""
입력: 컴퓨터의 수
연결되어 있는 컴퓨터 쌍의 수 
연결 정보 

출력: 1번 컴퓨터를 기준으로 바이러스에 걸리는 컴퓨터 수 
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
# 서로 연관이 있으니 index는 value들과 연결되어 있다!
visited = [False for _ in range(n+1)]
cnt = 0


def dfs(x):
    global cnt
    visited[x] = True  # 방문처리
    cnt += 1
    for i in g[x]:
        if visited[i]:  # 방문한 곳이라면
            continue  # 생략
        dfs(i)


dfs(1)
print(cnt-1)  # 자기자신 방문은 제외한다.

# from collections import deque
# def bfs(x):
#     q = deque([x])
#     cnt = 0
#     visited[x] = True
#     while q:
#         node = q.popleft()
#         for next_node in g[node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 q.append(next_node)
#                 cnt += 1
#     return cnt
