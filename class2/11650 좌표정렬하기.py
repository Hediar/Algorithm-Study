import sys

n = int(input())
result = []
for _ in range(n):
    result.append(sys.stdin.readline().rstrip().split())

result.sort(key=lambda x: (int(x[0]), int(x[1])))  # x를 먼저 기준으로, 다음은 y를 기준으로


for i in range(n):
    print(int(result[i][0]), int(result[i][1]))
