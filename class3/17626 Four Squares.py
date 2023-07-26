import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 1, 2]

# dp[N] = min(dp[k]) + 1

for i in range(3, n+1):
    j = 1 # 제곱수
    k = 4 # 완전 제곱수의 개수 
    while(j ** 2) <= i:
        k = min(k, dp[i - j**2])
        j += 1
    dp.append(k + 1)
print(dp[n])