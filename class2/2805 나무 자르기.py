import sys
n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(h)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in h:
        if i >= mid:
            total += i - mid  # 자르고 남은 길이

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
