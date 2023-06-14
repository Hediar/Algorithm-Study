"""
입력
계단의 개수
계단에 쓰여져 있는 점수

i번째 계단에 도달하는 방법
1. i-3 → i-2 → i
2. i-1 → i
"""

n = int(input())
step = [0]*(n+1)
dp = [0]*(n+1)

for i in range(1, n+1):
    step[i] = int(input())


if n == 1:
    print(step[1])

elif n == 2:
    print(step[1] + step[2])

else:
    dp[1] = step[1]
    dp[2] = step[1] + step[2]
    dp[3] = max(step[2] + step[3], step[1] + step[3])

    for i in range(4, n+1):
        dp[i] = max(dp[i-3] + step[i] + step[i-1], dp[i-2] + step[i])
        # i-3 ~ i 까지 두걸음 건너는 경우
        # ->  i-3에서의 최대 총점(dp) + 저장되어있는 각 계단의 점수
        # i-2 ~ i 까지 한걸음 건너는 경우

    print(dp[n])
