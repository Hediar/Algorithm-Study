import sys
input = sys.stdin.readline

n = int(input())
g= [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if g[i][k] and g[k][j]: # i -> k, k -> j 경로가 있으면 최단경로를 갱신해준다
                g[i][j] = 1

for i in range(n):
    for j in range(n):
        print(g[i][j], end=" ")
    print()