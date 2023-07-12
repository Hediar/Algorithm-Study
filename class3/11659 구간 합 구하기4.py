import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int, input().split()))

# 누적합 
for i in range(n-1):
    arr[i+1] += arr[i]
arr = [0] + arr # 1부터 시작하니 맨 처음에 빈 공간 만들어주기


for _ in range(m): # 구하고 싶은 것
    i, j = map(int,input().split())
    print(arr[j] - arr[i-1])