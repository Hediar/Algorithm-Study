"""
- 입력
    F : 총 층 개수
    S : 현재 위치한 층
    G : 목표 층
    U : 위로 U층을 가는 버튼
    D : 아래로 D층을 가는 버튼

- 출력
    S에서 G로 가기 위해 눌러야 하는 버튼의 수 최솟값
    이동할 수 없을 때에는 "use the stairs”출력
"""

import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)




def bfs(start, target):
    q = deque() 

    q.append(start)
    visited[start] = 1 # 시작점 방문처리 
    while q:
        x = q.popleft()

        if x == target:
            print(visited[x]-1)
            exit()
        
        for i in (x + U, x - D):
            if 0 < i <= F and visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
    print('use the stairs')

bfs(S,G)