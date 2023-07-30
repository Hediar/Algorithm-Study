import sys
input = sys.stdin.readline
n = int(input())
"""dp

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

"""

arr = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수라면 1, 아니면 0 저장
mincnt = 4
for i in range(int(n**0.5),0, -1): # n의 제곱근 ~ 1
    if arr[n]: # n이 제곱수일 경우
        mincnt = 1
        break
    elif arr[n - i**2]: # 나머지가 제곱수일 때
        mincnt = 2
        break
    else:
        for j in range(int((n - i**2) **0.5), 0, -1):
            if arr[(n - i**2) - j**2]:
                mincnt = 3

print(mincnt)