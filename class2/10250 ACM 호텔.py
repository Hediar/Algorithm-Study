t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    y = n % h  # 층
    x = n // h + 1  # 호
    if n % h == 0:
        y = h  # 층수는 높이
        x = n // h
    print(str(y*100 + x))
