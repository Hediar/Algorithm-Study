import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0

for i in range(n):
    result += sum(p[:i+1])

print(result)