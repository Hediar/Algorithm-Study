import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    a = int(input())
    coins.append(a)
coins.sort(reverse=True) # 가장 큰 값부터 나누기 위해 오름차순으로 된 것을 뒤집어준다.

result = 0

for i in coins:
    if k == 0:
        break # k가 0이 될 때 다 나누어졌으니 for문을 빠져나온다.
    result += k // i # 몫이 들어갈 수 있는 동전의 개수
    k %= i # 나머지는 다음으로 작은 동전으로 나누어주어야 한다. 
print(result)