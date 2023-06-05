"""
입력 : N 
N줄의 N개의 정수

출력: -1 종이의 개수, 0 종이의 개수, 1 종이의 개수 

"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0, 0]


def check(x, y, n):  # 시작점, 크기
    global cnt
    pick = m[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if pick != m[i][j]:  # 종류가 다를때
                new_n = n // 3  # 영역을 3/1분할
                for mi in range(0, 3):
                    for mj in range(0, 3):
                        check(x + mi*new_n, y + mj*new_n, new_n)
                return
    cnt[pick] += 1


check(0, 0, N)
for i in range(-1, 2):
    print(cnt[i])
