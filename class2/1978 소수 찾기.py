n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in a:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:  # 맨 끝에 도달했을때까지 나누어 떨어진 것이 없으면
                cnt += 1

            break  # 끝이 아닌데 나머지가 없으면 소수가 아니다.
print(cnt)
