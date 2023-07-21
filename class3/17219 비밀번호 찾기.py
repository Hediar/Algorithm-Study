import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for i in range(N):
    key, value = input().split()
    dict[key] = value

for j in range(M):
    find = input().strip()
    print(dict[find])