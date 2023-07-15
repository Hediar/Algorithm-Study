import sys
input = sys.stdin.readline

n = int(input())
result = [0, 1, 2, 3, 5]

for i in range(5, n+1):
    result.append(result[i-1] + result[i-2])

print(result[n]%10007)