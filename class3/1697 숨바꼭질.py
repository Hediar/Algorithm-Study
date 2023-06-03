"""
입력값 
수빈이 위치 N, 동생 위치 K

출력값
수빈이가 동생을 찾는 가장 빠른 시간 

수빈이는 이동이 가능하다.
걷기 : 1초 후  x-1 or x+1
순간이동: 1초 후 2*x

BFS를 사용한다. 
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

nm_max = 100000
visited = [0]*(nm_max+1)


def BFS():
    q = deque()
    # 출발위치
    q.append(n)

    while q:
        x = q.popleft()
        # 같은 위치가 되면 종료
        if x == k:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= nm_max and visited[i] == 0:
                visited[i] = visited[x]+1
                q.append(i)


BFS()
