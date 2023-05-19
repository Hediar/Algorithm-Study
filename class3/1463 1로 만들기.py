import sys
n = int(sys.stdin.readline())

dp = [0] * (n+1)  # d[1]을 첫번째로 만들어준다.

for i in range(2, n+1):  # 정수 2부터 n까지
    dp[i] = dp[i - 1] + 1  # 1로 빼는 경우
    if i % 3 == 0:  # 3으로 나누는 경우
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:  # 2로 나누는 경우
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])
