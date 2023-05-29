import sys

n = int(input())
result = []
for _ in range(n):
    result.append(sys.stdin.readline().rstrip().split())

result.sort(key=lambda x: (int(x[1]), int(x[0])))  # y를 먼저 우선으로


for i in range(n):
    print(int(result[i][0]), int(result[i][1]))
