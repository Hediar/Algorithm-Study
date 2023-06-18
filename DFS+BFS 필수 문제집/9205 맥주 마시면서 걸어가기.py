"""
- 입력
테스트 케이스 수 t

편의점 개수 n
상근이네 집 좌표
편의점 좌표
페스티벌 좌표 

- 출력
페스티벌 도착 시 happy
맥주가 바닥나서 이동을 못할 경우 sad
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def bfs():
    q = deque()
    q.append((home_x, home_y))

    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:  # 거리가 맥주를 다 마실때 내에 들어갈때
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                n_x, n_y = g[i]
                if abs(n_x - x) + abs(y-n_y) <= 1000:  # 현재 위치와 편의점 사이의 거리
                    visited[i] = 1
                    q.append((n_x, n_y))
    print("sad")
    return


for _ in range(T):
    n = int(input())  # 편의점 개수
    home_x, home_y = map(int, input().split())  # 상근이네 집
    g = []
    for _ in range(n):  # 편의점
        x, y = map(int, input().split())
        g.append((x, y))

    festival_x, festival_y = map(int, input().split())  # 페스티벌
    visited = [0 for _ in range(n+1)]

    bfs()
