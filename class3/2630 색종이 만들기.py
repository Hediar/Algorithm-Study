"""
입력
1. 한 변의 길이 n
m x m 만큼 각 숫자들이 입력 
"""
import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0


def check(x, y, n):
    global blue, white
    color = m[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != m[i][j]:  # 하나씩 검사하다가 다른 색이 있으면 잘라야한다.
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1


check(0, 0, N)
print(white)
print(blue)
