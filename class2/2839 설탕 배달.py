n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0:  # 5로 나누어 떨어지면
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
